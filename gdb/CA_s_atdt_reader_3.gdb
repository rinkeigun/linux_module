# script file name :CA_s_atdt_reader_3.gdb
# ファイルの取り込み
# (gdb) source CA_s_atdt_reader_3.gdb
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
	shell date > ~/ut/result/CA_s_atdt_reader_3.txt
	set logging file ~/ut/result/CA_s_atdt_reader_3.txt
	set logging on
	set pagination 0

	set var $cnt_reader_1 = 0 
	set var $counter = 0 


	set var $linenum = 99 
	#CA_s_atdt_reader_3.c:
	break CA_s_atdt_reader_3.c:$linenum
	commands
		silent
		#p $cnt_reader_1 ++	
		printf "\nbreakpoint : CA_s_atdt_reader_3.c:99\n" 
		printf "No. 8 r_ctx->rx_data==NULL 69行にbreakを設定\n"
		input_output
		cont
	end

	#シミュレータがないので、直接gdbからデータ入力
	set var $linenum = 72
	#CA_s_atdt_reader_3.c:
	break CA_s_atdt_reader_3.c:$linenum
	commands
		silent
		printf "\nNo.8, 9 breakpoint : CA_s_atdt_reader_3.c:\n"
		if $counter % 5 == 0
			p "case 0"
		end
		if $counter % 5 == 1
			set var r_ctx->rx_data = p_ctx->run_param
			p "case 1"
		end
		if $counter % 5 == 2
			set var r_ctx->rx_data = p_ctx->run_param
			p "case 2"
		end
		if $counter % 5 == 3
			set var r_ctx->rx_data = p_ctx->run_param
			p "case 3"
		end
		if $counter % 5 == 4
			set var r_ctx->rx_data = p_ctx->run_param
			p "case 4"
		end
		set var $counter ++
		#cont
	end

	b CA_s_atdt_reader_3.c:122
	commands
		silent
		set var r_ctx->rx_data->rsp_value[0] = s_size
		cont
	end

	b CA_s_atdt_reader_3.c:136
	commands
		silent
		set var bcc_failed = 0
		cont
	end

	b CA_s_atdt_reader_3.c:149
	commands
		silent
		set var data_number = r_ctx->trans_data_no
		cont
	end

	set var $linenum = 178
	#CA_s_atdt_reader_3.c:
	break CA_s_atdt_reader_3.c:$linenum
	commands
		silent
		printf "\nNo.9 breakpoint : CA_s_atdt_reader_3.c:178\n"
		input_output
		cont
	end

	set var $linenum = 1923
	#CA_PC_common.c:
	break CA_PC_common.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CA_PC_common.c:1923\n"
		printf "出力データcnv(%d)の検証\n", cnv
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

	break convert_atdt_2
	commands
		silent
		printf "\nbreakpoint : canvert_atdt_2(関数)\n"
		printf "No. 1 出力データstdの検証\n"
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
		printf "\nbreakpoint : CASL_std_log.c:423\n"
		p "No.2 sdataの出力の検証"
		p ((S_DATA *)sdata)[0]@sizeof(sdata)/4
		p "No. 3 nameの出力の検証"
		p name[0]@sizeof(name)/4
		cont
	end



	set var $linenum = 1687
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CAL_sysparam.c:1678\n"
		p "No.14 sptW->s_attr.attr.atdt.systemの値の検証"
		p sptW->s_attr.attr.atdt.system
		cont
	end

	break CAL_sysparam.c:1999
	commands
		silent
		printf "\nsnp1 ->"
		cont
	end

	break CAL_sysparam.c:2002
	commands
		silent
		printf "snp2 ->"
		cont
	end

	break CAL_sysparam.c:2025
	commands
		silent
		printf "STYPE_ATDT ->"
		cont
	end

	break CAL_sysparam.c:2028
	commands
		silent
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_at, snp2->s_attr.attr.atdt.system_at 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_rh, snp2->s_attr.attr.atdt.system_rh 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_ra, snp2->s_attr.attr.atdt.system_ra 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_sn, snp2->s_attr.attr.atdt.system_sn 
		cont
	end

	set var $linenum = 2033
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CAL_sysparam.c:2033\n"
		p "No.15 at, rh, ra, snの値の検証"
		p " snp1->s_attr.attr.atdt == snp2->s_attr.attr.atdt"
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_at, snp2->s_attr.attr.atdt.system_at 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_rh, snp2->s_attr.attr.atdt.system_rh 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_ra, snp2->s_attr.attr.atdt.system_ra 
		printf "at %d, %d\n", snp1->s_attr.attr.atdt.system_sn, snp2->s_attr.attr.atdt.system_sn 
		cont
	end

	break CAL_sysparam.c:3604
	commands
		silent
		printf "CAL_LOCAL_FL = %d ->", status
		cont
	end
	break CAL_sysparam.c:3606
	commands
		silent
		printf "xmlsts ?= 1 ->" 
		cont
	end

	break CAL_sysparam.c:3608
	commands
		silent
		printf "ntype = %d ->" , ntype
		cont
	end


	set var $linenum = 3656
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CAL_sysparam.c:3656\n"
		p "No.16 status, xmlsts, prmの値の検証"
		printf "status = %d, xmlsts = %d\n", status, xmlsts 
		print prm[0]
		cont
	end

	set var $linenum = 3820
	#CAL_sysparam.c:
	break CAL_sysparam.c:$linenum
	commands
		silent
		printf "\nbreakpoint : CAL_sysparam.c:3820\n"
		p "No.17 tabtbl, txttbl値の検証"
		print "tabtbl\n" 
		p ((CAL_TAB_TBL *)tabtbl)[0]@sizeof(tabtbl)/sizeof(CAL_TAB_TBL)
		print "txttbl\n" 
		p ((CAL_TEXT_TBL *)txttbl)[0]@sizeof(txttbl)/sizeof( CAL_TEXT_TBL )
		cont
	end

	run
end
document print_db
	usage : print_db
end
	
