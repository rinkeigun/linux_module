# script file name :signal.gdb
# ファイルの取り込み
# (gdb) source signal.gdb
# スクリプトの実行
# (gdb) set_data

define set_data
	set logging file ~user1/ut/result/signal.txt
	set logging on
	set pagination 0
	handle SIGUSR1 nostop
	shell date

	break sender.c:411
	commands
	silent
		print "411"
		cont
	end

	break sender.c:424
	commands
	silent
		print "424"
		cont
	end

	break sender.c:427
	commands
	silent
		print "427"
		cont
	end

	break sender.c:444
	commands
	silent
		print "444"
		cont
	end

	break sender.c:455
	commands
	silent
		print "455"
		cont
	end

	break sender.c:459
	commands
	silent
		print "459"
		cont
	end


	break sender.c:510
	commands
	silent
		print "510"
		cont
	end


	break sender.c:519
	commands
	silent
		print "519"
		cont
	end


	break sender.c:652
	commands
	silent
		print "652"
		cont
	end

	break sender.c:829
	commands
	silent
		print "829"
		cont
	end

	break sender.c:831
	commands
	silent
		print "831"
		cont
	end


	break sender.c:859
	commands
	silent
		print "       859"
		cont
	end


	break sender.c:860
	commands
	silent
		print "       860"
		cont
	end


end

document set_data
	usage : set_data
end
	
