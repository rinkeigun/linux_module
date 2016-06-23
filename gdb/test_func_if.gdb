# (gdb) source test_func_if.gdb
# スクリプトの実行
# (gdb) print_db

define print_db
	shell date > test_func_if.txt
	set logging file test_func_if.txt
	set logging on
	set pagination 0

	break func1
	commands
		silent
		#printf "%d\n",j 
		#関数内部に入っているので呼び出し側の変数jを参照できない
		printf "%d\n",a 
		cont
	end

	break 12
	commands
		silent
		printf "12行 %d\n",i 
		cont
	end

	break 13
	commands
		silent
		printf "13行 %d\n",i 
		cont
	end

	break 15
	commands
		silent
		printf "15行 %d\n",i 
		cont
	end



	run
end
document print_db
	usage : print_db
end
	
