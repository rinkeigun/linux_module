# script file name :CA_s_atdt_reader_1.gdb
# ファイルの取り込み
# (gdb) source CA_s_atdt_reader_1.gdb
# スクリプトの実行
# (gdb) print_db
define input_output
		p "入出力データ(sys_ctx->sys.processor->sensor->s_attr.attr.atdt   ->    stds)の検証"
		printf "at 入力:%d, 出力:%d\n", sys_ctx->sys.processor->sensor->s_attr.attr.atdt.system_at, stds->system_at->value->itype
		printf "rh 入力:%d, 出力:%d\n", sys_ctx->sys.processor->sensor->s_attr.attr.atdt.system_rh, stds->system_rh->value->itype
		printf "ra 入力:%d, 出力:%d\n", sys_ctx->sys.processor->sensor->s_attr.attr.atdt.system_ra, stds->system_ra->value->itype
		printf "sn 入力:%d, 出力:%d\n", sys_ctx->sys.processor->sensor->s_attr.attr.atdt.system_sn, stds->system_sn->value->itype
end

define print_db
	#$output_file = "~/ut/result/"
	shell date > ~/ut/result/CA_s_atdt_reader_1.txt
	set logging file ~/ut/result/CA_s_atdt_reader_1.txt
	set logging on
	set pagination 0

	set var $linenum = 113
	#CA_s_atdt_reader_1.c:
	break CA_s_atdt_reader_1.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CA_s_atdt_reader_1.c:%d\n", $linenum
		printf "r_ctx->rx_data==NULL 69行にbreakを設定\n"
		input_output
		cont
	end

	set var $linenum = 178
	#CA_s_atdt_reader_1.c:
	break CA_s_atdt_reader_1.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CA_s_atdt_reader_1.c:%d\n", $linenum
		input_output
		cont
	end

	set var $linenum = 1923
	#CA_PC_common.c:
	break convert_atdt_2
	commands
		silent
		printf "\nbreakpoint : canvert_atdt_2(関数)\n"
		printf "入力データcnv(%d)の検証\n", cnv
		print "dat->main_sub_AT"
		print dat->main_sub_AT
		print "dat->main_sub_RH"
		print dat->main_sub_RH
		print "dat->main_sub_RA"
		print dat->main_sub_RA
		print "dat->main_sub_SN"
		print dat->main_sub_SN
		cont
	end

	break CA_PC_common.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CA_PC_common.c:%d\n", $linenum
		printf "出力データstdの検証\n"
		print "std->sensor->system_at"
		print std->sensor->system_at
		print "std->sensor->system_rh"
		print std->sensor->system_rh
		print "std->sensor->system_ra"
		print std->sensor->system_ra
		print "std->sensor->system_sn"
		print std->sensor->system_sn
		cont
	end

	set var $linenum = 423
	#CASL_std_log.c:
	break CASL_std_log.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CASL_std_log.c:%d\n", $linenum
		p "sdataの出力の検証"
		p ((S_DATA *)sdata)[0]@sizeof(sdata)/4
		p "nameの出力の検証"
		p name[0]@sizeof(name)/4
		cont
	end


	run
end
document print_db
	usage : print_db
end
	
