# script file name UT_No13.gdb
# ファイルの取り込み
# (gdb) source UT_No13.gdb
# スクリプトの実行
# (gdb) print_db

define print_db
	#$output_file = "~/ut/result/"
	shell date > ~/ut/result/UT_No13.txt
	set logging file ~/ut/result/UT_No13.txt
	set logging on
	set pagination 0

	set var $cnt_reader_1 = 0 

	set var $linenum = 7072
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum
	commands
		silent
		printf "\nbreakpoint mor : CAL_sysparam.c:7072\n" 
		printf "ename = %s\n", ename
		cont
	end

	set var $linenum = 7296
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum if strcmp(ename , "mor" ) == 0
	commands
		silent
		printf "\nbreakpoint mor : CAL_sysparam.c:7296\n" 
		printf "ename = %s\n", ename
		print tabtbl[itab].prm 
		print edtag 
		cont
	end

	set var $linenum = 2377
	#CAL_sysparam.c:
	break CA_db_sender_2_body.c:$linenum
	commands
		silent
		printf "\nbreakpoint mor : CA_db_sender_2_body.c:2377\n"
		printf "use = %c, select = %c\n", bfm->mor.use, bfm->mor.select
		cont
	end

	set var $linenum = 2387
	#CA_db_sender_2_body.c:
	break CA_db_sender_2_body.c:$linenum
	commands
		silent
		printf "\nbreakpoint mor : CA_db_sender_2_body.c:2387\n"
		printf "select = 1\n"
		cont
	end

	set var $linenum = 2413
	#CA_db_sender_2_body.c:
	break CA_db_sender_2_body.c:$linenum
	commands
		silent
		printf "\nbreakpoint mor : CA_db_sender_2_body.c:2413\n"
		printf "select = 0\n"
		cont
	end

	set var $linenum = 2996
	#CA_db_sender_2_body.c:
	break CA_db_sender_2_body.c:$linenum
	commands
		silent
		printf "\nbreakpoint mor : CA_db_sender_2_body.c:2996\n"
		printf "ii = %d, jj = %d, blknum1 = %d\n", ii, jj, blknum1
		p mhdp->ddhhmm
		p mhdp->ddhhmm[2]
		p dinp->date
		p dinp->time
		cont
	end

	run
end
document print_db
	usage : print_db
end
	
