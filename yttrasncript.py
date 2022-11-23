from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
youtube_video = "https://www.youtube.com/watch?v=A4OmtyaBHFE"
video_id = youtube_video.split("=")[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)
result = ""
for i in transcript:
result += ' ' + i['text']
n=len(result)
summarizer = pipeline('summarization')
num_iters = int(n/1000)
summarized_text = []
for i in range(0, num_iters + 1):
start = 0
start = i * 1000
end = (i + 1) * 1000
print("input text \n" + result[start:end])
out = summarizer(result[start:end])
out = out[0]
out = out['summary_text']
print("Summarized text\n"+out)
summarized_text.append(out)
