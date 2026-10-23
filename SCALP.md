# Range-Scalp Bot

*Updated Fri Oct 23 01:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29598 | 25759 | 3839 (39) | 1 | $-8759.51 | -4.7% |
| **+10¢** | 22200 | 17757 | 4443 (55) | 1 | $-7881.17 | -5.6% |
| **+15¢** | 18587 | 13817 | 4770 (78) | 1 | $-7063.22 | -6.1% |
| **+20¢** | 16451 | 11452 | 4999 (100) | 1 | $-6392.09 | -6.2% |
| **+10¢ (15¢ stop)** | 36350 | 36291 | 59 (32) | 1 | $-13723.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 01:53 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-23 01:51 | +10 stop | HYPE | UP | 0.64 | 0.46 | -2.19 |
| 10-23 01:51 | +20 | HYPE | UP | 0.64 | open |  |
| 10-23 01:51 | +15 | HYPE | UP | 0.63 | open |  |
| 10-23 01:51 | +10 | HYPE | UP | 0.62 | open |  |
| 10-23 01:51 | +5 | HYPE | UP | 0.62 | open |  |
| 10-23 01:43 | +10 stop | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +20 | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +15 | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +10 | DOGE | UP | 0.71 | 0.93 | 2.03 |
| 10-23 01:43 | +5 | DOGE | UP | 0.71 | 0.93 | 2.03 |
| 10-23 01:43 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:43 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:43 | +5 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:42 | +10 stop | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +15 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +10 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +5 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +20 | BNB | UP | 0.56 | 0.92 | 3.37 |
| 10-23 01:42 | +15 | BNB | UP | 0.56 | 0.73 | 1.38 |
| 10-23 01:42 | +10 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +5 | SOL | UP | 0.66 | 0.78 | 0.94 |
| 10-23 01:42 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:42 | +20 | SOL | UP | 0.70 | 0.94 | 2.21 |
| 10-23 01:42 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:42 | +10 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:41 | +10 stop | HYPE | DOWN | 0.68 | 0.37 | -3.43 |
| 10-23 01:41 | +20 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-23 01:41 | +15 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-23 01:41 | +10 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-23 01:41 | +5 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-23 01:33 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 01:33 | +20 | NEAR | DOWN | 0.65 | 0.93 | 2.54 |
| 10-23 01:33 | +15 | NEAR | DOWN | 0.65 | 0.93 | 2.54 |
| 10-23 01:33 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 01:33 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 01:33 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
