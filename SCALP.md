# Range-Scalp Bot

*Updated Wed Oct 21 01:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26482 | 23064 | 3418 (33) | 0 | $-7725.77 | -4.6% |
| **+10¢** | 19926 | 15981 | 3945 (48) | 0 | $-6803.25 | -5.4% |
| **+15¢** | 16677 | 12432 | 4245 (72) | 0 | $-6064.20 | -5.8% |
| **+20¢** | 14761 | 10309 | 4452 (91) | 0 | $-5456.25 | -5.9% |
| **+10¢ (15¢ stop)** | 32434 | 32381 | 53 (30) | 0 | $-11852.07 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 01:02 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-21 01:02 | +20 | HYPE | DOWN | 0.64 | 0.86 | 1.90 |
| 10-21 01:02 | +15 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-21 01:02 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-21 01:02 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-21 01:00 | +10 stop | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-21 01:00 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-21 01:00 | +15 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 10-21 01:00 | +10 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-21 01:00 | +5 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-21 00:55 | +10 stop | BTC | UP | 0.60 | 0.42 | -2.15 |
| 10-21 00:54 | +10 stop | XRP | UP | 0.58 | 0.26 | -3.52 |
| 10-21 00:54 | +10 stop | SOL | UP | 0.59 | 0.35 | -2.73 |
| 10-21 00:54 | +20 | SOL | UP | 0.59 | no | -6.07 |
| 10-21 00:54 | +15 | SOL | UP | 0.59 | no | -6.07 |
| 10-21 00:54 | +10 | SOL | UP | 0.59 | no | -6.07 |
| 10-21 00:54 | +5 | SOL | UP | 0.59 | no | -6.07 |
| 10-21 00:54 | +10 stop | HYPE | UP | 0.68 | 0.43 | -2.88 |
| 10-21 00:54 | +10 stop | BNB | UP | 0.66 | 0.36 | -3.33 |
| 10-21 00:54 | +20 | BNB | UP | 0.66 | no | -6.76 |
| 10-21 00:54 | +15 | BNB | UP | 0.66 | no | -6.76 |
| 10-21 00:54 | +10 | BNB | UP | 0.66 | no | -6.76 |
| 10-21 00:54 | +5 | BNB | UP | 0.66 | no | -6.76 |
| 10-21 00:52 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 10-21 00:52 | +20 | BTC | UP | 0.69 | no | -7.05 |
| 10-21 00:52 | +15 | BTC | UP | 0.69 | no | -7.05 |
| 10-21 00:52 | +10 | BTC | UP | 0.69 | no | -7.05 |
| 10-21 00:52 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 10-21 00:52 | +10 stop | HYPE | UP | 0.56 | 0.73 | 1.38 |
| 10-21 00:50 | +10 stop | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-21 00:50 | +10 | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-21 00:50 | +5 | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-21 00:50 | +10 stop | HYPE | DOWN | 0.52 | 0.21 | -3.40 |
| 10-21 00:50 | +20 | HYPE | DOWN | 0.52 | 0.81 | 2.61 |
| 10-21 00:50 | +15 | HYPE | DOWN | 0.52 | 0.81 | 2.61 |
| 10-21 00:50 | +10 | HYPE | DOWN | 0.52 | 0.81 | 2.61 |
| 10-21 00:50 | +5 | HYPE | DOWN | 0.52 | 0.81 | 2.61 |
| 10-21 00:50 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-21 00:50 | +10 stop | DOGE | DOWN | 0.42 | 0.59 | 1.35 |
| 10-21 00:50 | +10 stop | XRP | DOWN | 0.47 | 0.31 | -1.93 |
