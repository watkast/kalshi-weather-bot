# Range-Scalp Bot

*Updated Wed Oct 21 13:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27262 | 23743 | 3519 (39) | 0 | $-7906.55 | -4.6% |
| **+10¢** | 20496 | 16429 | 4067 (55) | 0 | $-6984.85 | -5.4% |
| **+15¢** | 17161 | 12785 | 4376 (78) | 0 | $-6242.29 | -5.8% |
| **+20¢** | 15191 | 10604 | 4587 (98) | 0 | $-5607.86 | -5.9% |
| **+10¢ (15¢ stop)** | 33451 | 33392 | 59 (32) | 0 | $-12398.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 12:59 | +10 stop | HYPE | DOWN | 0.13 | 0.49 | 3.34 |
| 10-21 12:59 | +20 | HYPE | DOWN | 0.13 | 0.49 | 3.34 |
| 10-21 12:59 | +15 | HYPE | DOWN | 0.13 | 0.49 | 3.34 |
| 10-21 12:59 | +10 | HYPE | DOWN | 0.13 | 0.49 | 3.34 |
| 10-21 12:59 | +5 | HYPE | DOWN | 0.13 | 0.49 | 3.34 |
| 10-21 12:56 | +10 stop | XRP | UP | 0.60 | 0.78 | 1.50 |
| 10-21 12:56 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 10-21 12:54 | +15 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-21 12:54 | +10 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-21 12:54 | +5 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-21 12:54 | +10 stop | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 10-21 12:54 | +10 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 10-21 12:54 | +5 | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 10-21 12:54 | +10 stop | XRP | UP | 0.54 | 0.69 | 1.17 |
| 10-21 12:53 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.51 |
| 10-21 12:51 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-21 12:51 | +10 stop | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 10-21 12:51 | +20 | ZEC | UP | 0.65 | 0.87 | 1.96 |
| 10-21 12:51 | +15 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 10-21 12:51 | +10 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 10-21 12:51 | +5 | ZEC | UP | 0.66 | 0.74 | 0.50 |
| 10-21 12:51 | +5 | BNB | UP | 0.66 | 0.80 | 1.08 |
| 10-21 12:50 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-21 12:50 | +10 stop | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-21 12:49 | +10 stop | BNB | UP | 0.60 | 0.44 | -1.92 |
| 10-21 12:49 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 12:49 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 12:49 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-21 12:49 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 12:49 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 12:49 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 10-21 12:48 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-21 12:48 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 10-21 12:48 | +10 stop | DOGE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-21 12:48 | +5 | ZEC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-21 12:47 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.25 |
| 10-21 12:47 | +20 | XRP | DOWN | 0.63 | yes | -6.47 |
| 10-21 12:47 | +15 | XRP | DOWN | 0.63 | yes | -6.47 |
| 10-21 12:47 | +10 | XRP | DOWN | 0.63 | yes | -6.47 |
| 10-21 12:47 | +5 | XRP | DOWN | 0.64 | yes | -6.53 |
