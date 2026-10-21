# Range-Scalp Bot

*Updated Wed Oct 21 09:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26951 | 23465 | 3486 (39) | 3 | $-7860.77 | -4.6% |
| **+10¢** | 20276 | 16249 | 4027 (55) | 3 | $-6948.53 | -5.4% |
| **+15¢** | 16976 | 12645 | 4331 (78) | 4 | $-6201.85 | -5.8% |
| **+20¢** | 15032 | 10491 | 4541 (97) | 4 | $-5575.32 | -5.9% |
| **+10¢ (15¢ stop)** | 33053 | 32994 | 59 (32) | 1 | $-12224.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 09:11 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-21 09:11 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.12 |
| 10-21 09:11 | +5 | NEAR | UP | 0.64 | open |  |
| 10-21 09:11 | +10 stop | HYPE | UP | 0.36 | 0.57 | 1.75 |
| 10-21 09:09 | +10 stop | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 10-21 09:09 | +5 | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 10-21 09:09 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-21 09:09 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-21 09:08 | +10 stop | HYPE | DOWN | 0.55 | 0.39 | -1.93 |
| 10-21 09:08 | +10 | HYPE | DOWN | 0.53 | 0.64 | 0.71 |
| 10-21 09:08 | +5 | HYPE | DOWN | 0.53 | 0.64 | 0.71 |
| 10-21 09:08 | +5 | NEAR | DOWN | 0.51 | 0.64 | 0.95 |
| 10-21 09:07 | +10 stop | NEAR | DOWN | 0.66 | 0.42 | -2.74 |
| 10-21 09:07 | +5 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-21 09:07 | +10 stop | NEAR | DOWN | 0.51 | 0.63 | 0.85 |
| 10-21 09:06 | +10 stop | BTC | UP | 0.67 | 0.81 | 1.13 |
| 10-21 09:06 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 10-21 09:06 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-21 09:06 | +10 stop | DOGE | UP | 0.65 | 0.82 | 1.43 |
| 10-21 09:06 | +10 stop | ZEC | UP | 0.54 | 0.67 | 0.96 |
| 10-21 09:06 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-21 09:05 | +5 | XRP | UP | 0.67 | 0.78 | 0.81 |
| 10-21 09:05 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.24 |
| 10-21 09:05 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-21 09:04 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 10-21 09:04 | +10 stop | BNB | UP | 0.63 | 0.82 | 1.62 |
| 10-21 09:04 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-21 09:04 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 10-21 09:04 | +10 stop | XRP | UP | 0.70 | 0.53 | -2.03 |
| 10-21 09:04 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-21 09:04 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-21 09:04 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-21 09:03 | +10 stop | DOGE | DOWN | 0.58 | 0.38 | -2.35 |
| 10-21 09:03 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-21 09:03 | +10 stop | BTC | DOWN | 0.57 | 0.39 | -2.15 |
| 10-21 09:03 | +10 stop | BNB | DOWN | 0.57 | 0.38 | -2.29 |
| 10-21 09:03 | +10 stop | NEAR | DOWN | 0.57 | 0.42 | -1.86 |
| 10-21 09:03 | +10 stop | SOL | DOWN | 0.60 | 0.45 | -1.85 |
| 10-21 09:03 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 10-21 09:03 | +20 | ZEC | DOWN | 0.71 | open |  |
