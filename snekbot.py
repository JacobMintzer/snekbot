import discord
from discord.ext import commands
import asyncio
import re
import random

bot = commands.Bot(command_prefix=['snek ', 'snekbot ', 'Snek ', 'snekbot2 ', 'Snekbot2 ', 'snek2 ', 'Snek2 ','SNEK '], description='Hssssss \nhi, am snekbot2, like snekbot but better and buffer')
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
	discord.opus.load_opus('opus')
@bot.event
@asyncio.coroutine 
def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	yield from bot.change_presence(game=discord.Game(type=0,name="snake"))

@bot.event
@asyncio.coroutine 
def on_message(message):
	if message.content.startswith('Snek suggest') or message.content.startswith('snek suggest'):
		yield from bot.send_message(message.channel,'thank you {0} for the suggestion, snek will work on it'.format(message.author.name))
		suggestion_obj=open("suggest.txt","a+")
		suggestion_obj.write(message.author.name+": "+message.content+'\n');
	elif message.content.startswith('snek shut up') or message.content.startswith('Snek shut up'):
		yield from bot.send_message(message.channel,'exCUSE me FUCKer but who the FUCK do you THINk you aRe')
	yield from bot.process_commands(message)

@bot.event
@asyncio.coroutine 
##
#def on_member_join(member):
#	if format(member.server)=='[S]quad':
		# yield from bot.send_message(member.server, 'Welcome {0}!'.format(member))
#		yield from bot.send_message(member.server, 'Welcome to the [S]quad Discord!\nIf you have any questions, feel free to ask any of the mods')


@bot.command()
@asyncio.coroutine 
def hss(*, stuff_for_snek_to_say):
	"""says stuff"""
	yield from bot.say(stuff_for_snek_to_say)
	
#@bot.command()
#@asyncio.coroutine

#	yield from bot.say('http://i.imgur.com/n3XYGyI.png')

@bot.command()
@asyncio.coroutine 
def pls():
	"""try it"""
	yield from bot.say(':snake:')
@bot.command()
@asyncio.coroutine 
def plsno():
    """pls no this is a bad idea u will regret it"""
    for x in range(0, 5):
        yield from bot.say('snek pls') # spaces > tabs

@bot.command()
@asyncio.coroutine 
def hello():
	"""hi"""
	yield from bot.say('hello yes this is snek.')
@bot.command()
@asyncio.coroutine 
def hi():
	"""hello"""
	yield from bot.say('hi yes this is snek.')

@bot.command()
@asyncio.coroutine 
def intensifies():
	"""[SNEK INTENSIFIES]"""
	yield from bot.say('http://i.imgur.com/hSZfCiD.gif')
@bot.command()
@asyncio.coroutine 
def noboop():
	"""noboop snek"""
	yield from bot.say('http://i.imgur.com/j4p70OX.jpg')
@bot.command()
@asyncio.coroutine 
def step():
	"""no step on snek"""
	yield from bot.say('http://i.imgur.com/SSkvSQL.jpg')
@bot.command()
@asyncio.coroutine 
def nervous():
	"""nervous hissing"""
	yield from bot.say('http://i.imgur.com/b6s9WTJ.gif')
@bot.command()
@asyncio.coroutine 
def art():
	"""jacob's beautiful art"""
	yield from bot.say (random.choice(['https://farm2.staticflickr.com/1622/24885440680_02487a7356_o_d.gif' , 'https://farm6.staticflickr.com/5700/23833016945_7cab5c3e92_o_d.png']))
@bot.command()
@asyncio.coroutine 
def smug():
	"""u srs askin snek what smug is?"""
	yield from bot.say ('http://orig09.deviantart.net/6e2f/f/2010/132/d/7/5th_gen_starter___tsutaaja_by_arkeis_pokemon.png')

	
@bot.command()
@asyncio.coroutine 
def play(*, game_to_play):
	"""snek likes playing game"""
	yield from bot.change_presence(game=discord.Game(type=0,name=game_to_play))
	
@bot.command()
@asyncio.coroutine 
def stream(*, game_to_play):
	"""snek likes streaming game"""
	#yield from bot.change_presence(game=discord.Game(name=game_to_play))
	yield from bot.change_presence(game=discord.Game(type=1,name=game_to_play,url='https://go.twitch.tv/pokespeedrunbots'))

	
@bot.command()
@asyncio.coroutine 
def ily():
	"""tell snek ily"""
	yield from bot.say('snek loves yogurt 2')



@bot.command()
@asyncio.coroutine 
def bully(member : discord.User = bot.user):
	"""watch out, snek will bully u"""
	bully_reply=[]
	bully_object=open("bully.txt","r")
	while 1:
		line = bully_object.readline()
		if not line:
			break	
		else:
			bully_reply.append(line)
	yield from bot.say(random.choice(bully_reply).format(member.mention))

@bot.command()
@asyncio.coroutine 
def push():
	yield from bot.say('snek is PUSHING BUTTONS')
	
@bot.command()
@asyncio.coroutine 
def jump():
	yield from bot.say('WHY U JUMPIN? PUSSYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
	
@bot.command()
@asyncio.coroutine 
def facebook():
	yield from bot.say('http://3.bp.blogspot.com/-LVwahNhtd9M/UcYXK8QycJI/AAAAAAAAF3I/8JH3xKlIJYI/s1600/troll+face.gif')
	
@bot.command()
@asyncio.coroutine 
def results():
	yield from bot.say ('snek got 3rd in an 8 person bracket once')
	
@bot.command()
@asyncio.coroutine 
def flirt():
	"""snek is smuuth"""
	flirt_reply=[]
	flirt_object=open("flirt.txt","r")
	while 1:
		line = flirt_object.readline()
		if not line:
			break	
		else:
			flirt_reply.append(line)
	yield from bot.say(random.choice(flirt_reply))
	
	
@bot.command()
@asyncio.coroutine 
def ifbully():
	"""to bully or not to bully"""
	yield from bot.say (random.choice(['http://i.imgur.com/NRMo4jZ.jpg' , 'http://i.imgur.com/7NEWEFu.jpg']))

@bot.command()
@asyncio.coroutine	
def live():
	yield from bot.say ('i have risen my son')

@bot.command()
@asyncio.coroutine 
def REE():
	"""REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""
	yield from bot.say('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
	
@bot.command()
@asyncio.coroutine 
def tendies():
	"""snek wants tendies"""
	yield from bot.say('MOM WHERE ARE MY TENDIES\nREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
	
@bot.command()
@asyncio.coroutine 
def sad():
	"""snek is sad"""
	yield from bot.say('https://cdn.drawception.com/images/panels/2012/3-31/8SMj5httsM-12.png')
	
@bot.command()
@asyncio.coroutine 
def whomade():
	"""who made snek?"""
	yield from bot.say('jacob made snekbot2 which was based off of SplitPixl\'s snekbot')
@bot.command()
@asyncio.coroutine 
def info():
	"""info about snekbot"""
	yield from bot.say('snekbot was coded in python with the library discord.py. hss.')
@bot.command()
@asyncio.coroutine 
def invite():
	"""snekbot invite link"""
	yield from bot.say('to add snekbot to your server click this: https://goo.gl/xqfKWn')
@bot.command()
@asyncio.coroutine 
def git():
	"""snek's source code"""
	yield from bot.say('https://github.com/JacobMintzer/snekbot')
	
#music stuff below
class VoiceEntry:
	def __init__(self, message, player):
		self.requester = message.author
		self.channel = message.channel
		self.player = player

	def __str__(self):
		fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
		duration = self.player.duration
		if duration:
			fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
		return fmt.format(self.player, self.requester)

class VoiceState:
	def __init__(self, bot):
		self.current = None
		self.voice = None
		self.bot = bot
		self.play_next_song = asyncio.Event()
		self.songs = asyncio.Queue()
		self.skip_votes = set() # a set of user_ids that voted
		self.audio_player = self.bot.loop.create_task(self.audio_player_task())

	def is_playing(self):
		if self.voice is None or self.current is None:
			return False

		player = self.current.player
		return not player.is_done()

	@property
	def player(self):
		return self.current.player

	def skip(self):
		self.skip_votes.clear()
		if self.is_playing():
			self.player.stop()

	def toggle_next(self):
		self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

	@asyncio.coroutine
	def audio_player_task(self):
		while True:
			self.play_next_song.clear()
			self.current = yield from self.songs.get()
			yield from self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
			self.current.player.start()
			yield from self.play_next_song.wait()

class Music:
	"""Voice related commands.
	Works in multiple servers at once.
	"""
	def __init__(self, bot):
		self.bot = bot
		self.voice_states = {}

	def get_voice_state(self, server):
		state = self.voice_states.get(server.id)
		if state is None:
			state = VoiceState(self.bot)
			self.voice_states[server.id] = state

		return state

	@asyncio.coroutine
	def create_voice_client(self, channel):
		voice = yield from self.bot.join_voice_channel(channel)
		state = self.get_voice_state(channel.server)
		state.voice = voice

	def __unload(self):
		for state in self.voice_states.values():
			try:
				state.audio_player.cancel()
				if state.voice:
					self.bot.loop.create_task(state.voice.disconnect())
			except:
				pass

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def join(self, ctx, *, channel : discord.Channel):
		"""Joins a voice channel."""
		try:
			yield from self.create_voice_client(channel)
		except discord.ClientException:
			yield from self.bot.say('Already in a voice channel...')
		except discord.InvalidArgument:
			yield from self.bot.say('This is not a voice channel...')
		else:
			yield from self.bot.say('Ready to play audio in ' + channel.name)

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def yell(self, ctx):
		"""Summons the bot to join your voice channel."""
		summoned_channel = ctx.message.author.voice_channel
		if summoned_channel is None:
			yield from self.bot.say('who snek yell at?')
			return False

		state = self.get_voice_state(ctx.message.server)
		if state.voice is None:
			state.voice = yield from self.bot.join_voice_channel(summoned_channel)
		else:
			yield from state.voice.move_to(summoned_channel)

		return True
		
	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def summon(self, ctx):
		"""Summons the bot to join your voice channel."""
		summoned_channel = ctx.message.author.voice_channel
		if summoned_channel is None:
			yield from self.bot.say('who snek yell at?')
			return False

		state = self.get_voice_state(ctx.message.server)
		if state.voice is None:
			state.voice = yield from self.bot.join_voice_channel(summoned_channel)
		else:
			yield from state.voice.move_to(summoned_channel)

		return True
		
	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine 
	def sit(self,ctx):
		state = self.get_voice_state(ctx.message.server)
		opts = {
			'default_search': 'auto',
			'quiet': True,
			"-q:a": 9,
		}

		if state.voice is None:
			success = yield from ctx.invoke(self.summon)
			if not success:
				return

		try:
			player = yield from state.voice.create_ytdl_player("GFsFCfgsehA", ytdl_options=opts, after=state.toggle_next)
		except Exception as e:
			fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
			yield from self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
		else:
			player.volume = 0.4
			entry = VoiceEntry(ctx.message, player)
			yield from self.bot.say('Enqueued ' + str(entry))
			yield from state.songs.put(entry)
		
	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine 
	def fart(self,ctx):
		state = self.get_voice_state(ctx.message.server)
		opts = {
			'default_search': 'auto',
			'quiet': True,
			"-q:a": 9,
		}

		if state.voice is None:
			success = yield from ctx.invoke(self.summon)
			if not success:
				return

		try:
			player = yield from state.voice.create_ytdl_player("https://soundcloud.com/all-my-farts/farts-all", ytdl_options=opts, after=state.toggle_next)
		except Exception as e:
			fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
			yield from self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
		else:
			player.volume = 0.4
			entry = VoiceEntry(ctx.message, player)
			yield from self.bot.say('Enqueued ' + str(entry))
			yield from state.songs.put(entry)
	
	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine 
	def add(self, ctx, *, song : str):
		"""Plays a song.
		If there is a song currently in the queue, then it is
		queued until the next song is done playing.
		This command automatically searches as well from YouTube.
		The list of supported sites can be found here:
		https://rg3.github.io/youtube-dl/supportedsites.html
		"""
		state = self.get_voice_state(ctx.message.server)
		opts = {
			'default_search': 'auto',
			'quiet': True,
			"-q:a": 9,
			
		}

		if state.voice is None:
			success = yield from ctx.invoke(self.summon)
			if not success:
				return

		try:
			player = yield from state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
		except Exception as e:
			fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
			yield from self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
		else:
			player.volume = 0.4
			entry = VoiceEntry(ctx.message, player)
			yield from self.bot.say('Enqueued ' + str(entry))
			yield from state.songs.put(entry)

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def volume(self, ctx, value : int):
		"""Sets the volume of the currently playing song."""
		state = self.get_voice_state(ctx.message.server)
		
		if value>100:
			yield from self.bot.say('fuck you john')	
		elif state.is_playing():
			player = state.player
			player.volume = value / 100
			yield from self.bot.say('Set the volume to {:.0%}'.format(player.volume))

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def pause(self, ctx):
		"""Pauses the currently played song."""
		state = self.get_voice_state(ctx.message.server)
		if state.is_playing():
			player = state.player
			player.pause()

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def resume(self, ctx):
		"""Resumes the currently played song."""
		state = self.get_voice_state(ctx.message.server)
		if state.is_playing():
			player = state.player
			player.resume()

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def stop(self, ctx):
		"""Stops playing audio and leaves the voice channel.
		This also clears the queue.
		"""
		server = ctx.message.server
		state = self.get_voice_state(server)

		if state.is_playing():
			player = state.player
			player.stop()

		try:
			state.audio_player.cancel()
			del self.voice_states[server.id]
			yield from state.voice.disconnect()
		except:
			pass

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def skip(self, ctx):
		"""Vote to skip a song. The song requester can automatically skip.
		3 skip votes are needed for the song to be skipped.
		"""

		state = self.get_voice_state(ctx.message.server)
		if not state.is_playing():
			yield from self.bot.say('Not playing any music right now...')
			return

		voter = ctx.message.author
		if voter == state.current.requester:
			yield from self.bot.say('Requester requested skipping song...')
			state.skip()
		elif voter.id not in state.skip_votes:
			state.skip_votes.add(voter.id)
			total_votes = len(state.skip_votes)
			if total_votes >= 3:
				yield from self.bot.say('Skip vote passed, skipping song...')
				state.skip()
			else:
				yield from self.bot.say('Skip vote added, currently at [{}/3]'.format(total_votes))
		else:
			yield from self.bot.say('You have already voted to skip this song.')

	@commands.command(pass_context=True, no_pm=True)
	@asyncio.coroutine
	def playing(self, ctx):
		"""Shows info about the currently played song."""

		state = self.get_voice_state(ctx.message.server)
		if state.current is None:
			yield from self.bot.say('Not playing anything.')
		else:
			skip_count = len(state.skip_votes)
			yield from self.bot.say('Now playing {} [skips: {}/3]'.format(state.current, skip_count))

bot.add_cog(Music(bot))
file_object=open("key.txt","r")
bot.run(file_object.read())