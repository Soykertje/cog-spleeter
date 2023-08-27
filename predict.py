import tempfile
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from cog import BasePredictor, Input, Path, BaseModel


class ModelOutput(BaseModel):
    vocals: Path
    accompaniment: Path


class Predictor(BasePredictor):

    def setup(self):
        """Loads Spleeter 2 stems model into memory from disk"""
        self.separator = Separator('spleeter:2stems')
        self.audio_loader = AudioAdapter.default()

    def predict(
            self,
            audio: Path = Input(description="Audio file")
    ) -> ModelOutput:
        """Separate the vocals from the accompaniment of an audio file"""
        waveform, sample_rate = self.audio_loader.load(str(audio))
        prediction = self.separator.separate(waveform)

        out_path = Path(tempfile.mkdtemp())

        out_path_vocals = out_path / "vocals.wav"
        out_path_accompaniment = out_path / "accompaniment.wav"

        self.audio_loader.save(str(out_path_vocals), prediction['vocals'], sample_rate)
        self.audio_loader.save(str(out_path_accompaniment), prediction['accompaniment'], sample_rate)

        return ModelOutput(
            vocals=out_path_vocals,
            accompaniment=out_path_accompaniment
        )
