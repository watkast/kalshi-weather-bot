# Range-Scalp Bot

*Updated Mon Nov 09 07:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53453 | 46602 | 6851 (85) | 0 | $-14794.36 | -4.4% |
| **+10¢** | 39929 | 31939 | 7990 (110) | 0 | $-13796.71 | -5.5% |
| **+15¢** | 33460 | 24851 | 8609 (141) | 1 | $-12594.34 | -6.0% |
| **+20¢** | 29775 | 20747 | 9028 (186) | 1 | $-11095.11 | -5.9% |
| **+10¢ (15¢ stop)** | 65140 | 65034 | 106 (63) | 0 | $-24119.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 07:05 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.54 |
| 11-09 07:03 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.11 |
| 11-09 07:03 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-09 07:03 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-09 07:01 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 07:01 | +20 | BTC | DOWN | 0.71 | 0.94 | 2.08 |
| 11-09 07:01 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-09 07:01 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-09 07:01 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-09 07:01 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-09 07:01 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 07:01 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 11-09 06:59 | +10 stop | HYPE | DOWN | 0.14 | 0.56 | 3.93 |
| 11-09 06:58 | +10 stop | HYPE | UP | 0.57 | 0.71 | 1.07 |
| 11-09 06:54 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-09 06:52 | +10 stop | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-09 06:50 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-09 06:50 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 11-09 06:50 | +10 stop | NEAR | UP | 0.60 | 0.40 | -2.34 |
| 11-09 06:49 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 11-09 06:48 | +10 stop | DOGE | UP | 0.59 | 0.74 | 1.19 |
| 11-09 06:48 | +10 stop | SOL | DOWN | 0.52 | 0.35 | -2.04 |
| 11-09 06:48 | +10 stop | BTC | UP | 0.60 | 0.82 | 1.92 |
| 11-09 06:48 | +10 stop | NEAR | DOWN | 0.62 | 0.46 | -1.95 |
| 11-09 06:47 | +10 stop | BNB | UP | 0.61 | 0.81 | 1.72 |
| 11-09 06:47 | +10 stop | ETH | UP | 0.65 | 0.78 | 0.97 |
| 11-09 06:47 | +10 stop | ZEC | DOWN | 0.61 | 0.40 | -2.44 |
| 11-09 06:47 | +20 | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-09 06:47 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-09 06:47 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-09 06:47 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-09 06:47 | +10 stop | HYPE | UP | 0.48 | 0.65 | 1.34 |
| 11-09 06:46 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 11-09 06:46 | +20 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-09 06:46 | +15 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-09 06:46 | +10 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-09 06:46 | +5 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-09 06:46 | +10 stop | BNB | DOWN | 0.60 | 0.33 | -3.03 |
| 11-09 06:46 | +20 | BNB | DOWN | 0.60 | yes | -6.17 |
| 11-09 06:46 | +15 | BNB | DOWN | 0.60 | yes | -6.17 |
