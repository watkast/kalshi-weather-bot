# Range-Scalp Bot

*Updated Mon Nov 23 10:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69814 | 60916 | 8898 (146) | 2 | $-18814.25 | -4.3% |
| **+10¢** | 52094 | 41698 | 10396 (189) | 2 | $-17505.87 | -5.3% |
| **+15¢** | 43658 | 32461 | 11197 (244) | 4 | $-15629.71 | -5.7% |
| **+20¢** | 38876 | 27096 | 11780 (309) | 4 | $-13974.06 | -5.7% |
| **+10¢ (15¢ stop)** | 85028 | 84838 | 190 (118) | 1 | $-31244.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 10:31 | +20 | SOL | UP | 0.71 | open |  |
| 11-23 10:31 | +5 | SOL | UP | 0.71 | open |  |
| 11-23 10:31 | +10 stop | SOL | UP | 0.71 | open |  |
| 11-23 10:31 | +15 | SOL | UP | 0.71 | open |  |
| 11-23 10:31 | +10 | SOL | UP | 0.71 | open |  |
| 11-23 10:30 | +10 stop | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 11-23 10:30 | +20 | HYPE | UP | 0.63 | open |  |
| 11-23 10:30 | +15 | HYPE | UP | 0.63 | open |  |
| 11-23 10:30 | +10 | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 11-23 10:30 | +5 | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 11-23 10:30 | +10 stop | ZEC | DOWN | 0.52 | 0.37 | -1.85 |
| 11-23 10:30 | +20 | ZEC | DOWN | 0.51 | open |  |
| 11-23 10:30 | +15 | ZEC | DOWN | 0.51 | open |  |
| 11-23 10:30 | +10 | ZEC | DOWN | 0.51 | open |  |
| 11-23 10:30 | +5 | ZEC | DOWN | 0.51 | open |  |
| 11-23 10:27 | +10 stop | BNB | DOWN | 0.71 | 0.38 | -3.62 |
| 11-23 10:27 | +10 stop | SOL | DOWN | 0.55 | 0.69 | 1.07 |
| 11-23 10:26 | +10 stop | DOGE | UP | 0.51 | 0.62 | 0.75 |
| 11-23 10:25 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-23 10:25 | +10 stop | HYPE | UP | 0.66 | 0.79 | 1.02 |
| 11-23 10:25 | +20 | HYPE | UP | 0.66 | 0.92 | 2.33 |
| 11-23 10:25 | +15 | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 11-23 10:25 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-23 10:25 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 11-23 10:25 | +5 | SOL | UP | 0.65 | no | -6.66 |
| 11-23 10:24 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-23 10:24 | +10 stop | DOGE | UP | 0.51 | 0.62 | 0.75 |
| 11-23 10:24 | +10 stop | BNB | DOWN | 0.69 | 0.53 | -1.93 |
| 11-23 10:24 | +10 | BNB | DOWN | 0.69 | yes | -7.05 |
| 11-23 10:24 | +10 stop | SOL | UP | 0.58 | 0.40 | -2.15 |
| 11-23 10:24 | +20 | SOL | UP | 0.58 | no | -5.98 |
| 11-23 10:24 | +15 | SOL | UP | 0.58 | no | -5.98 |
| 11-23 10:24 | +10 | SOL | UP | 0.58 | no | -5.98 |
| 11-23 10:24 | +5 | SOL | UP | 0.58 | 0.65 | 0.36 |
| 11-23 10:24 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-23 10:24 | +10 stop | BNB | UP | 0.41 | 0.61 | 1.66 |
| 11-23 10:22 | +10 stop | BTC | DOWN | 0.59 | 0.39 | -2.34 |
| 11-23 10:22 | +10 stop | ZEC | DOWN | 0.66 | 0.39 | -3.03 |
| 11-23 10:21 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.77 |
| 11-23 10:20 | +10 stop | BNB | DOWN | 0.63 | 0.41 | -2.54 |
