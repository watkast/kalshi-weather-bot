# Range-Scalp Bot

*Updated Sat Oct 17 17:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21293 | 18541 | 2752 (29) | 0 | $-6160.11 | -4.6% |
| **+10¢** | 16020 | 12840 | 3180 (41) | 0 | $-5497.85 | -5.5% |
| **+15¢** | 13394 | 9967 | 3427 (61) | 0 | $-4996.60 | -5.9% |
| **+20¢** | 11867 | 8276 | 3591 (80) | 1 | $-4447.10 | -6.0% |
| **+10¢ (15¢ stop)** | 26141 | 26091 | 50 (29) | 0 | $-9958.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 17:12 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 10-17 17:10 | +10 stop | BTC | UP | 0.67 | 0.49 | -2.14 |
| 10-17 17:10 | +10 stop | ETH | UP | 0.71 | 0.48 | -2.63 |
| 10-17 17:10 | +10 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-17 17:10 | +5 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-17 17:10 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-17 17:10 | +10 stop | XRP | UP | 0.53 | 0.25 | -3.12 |
| 10-17 17:09 | +5 | HYPE | DOWN | 0.52 | 0.58 | 0.24 |
| 10-17 17:09 | +10 stop | SOL | UP | 0.67 | 0.48 | -2.24 |
| 10-17 17:09 | +10 | ETH | UP | 0.60 | 0.75 | 1.23 |
| 10-17 17:08 | +5 | ETH | UP | 0.64 | 0.75 | 0.79 |
| 10-17 17:08 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-17 17:08 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-17 17:08 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-17 17:08 | +10 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-17 17:08 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-17 17:08 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.79 |
| 10-17 17:08 | +10 stop | DOGE | DOWN | 0.64 | 0.49 | -1.85 |
| 10-17 17:08 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 17:08 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 17:08 | +10 stop | XRP | DOWN | 0.62 | 0.37 | -2.84 |
| 10-17 17:08 | +20 | XRP | DOWN | 0.62 | 0.86 | 2.14 |
| 10-17 17:08 | +15 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 17:08 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 17:08 | +5 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 17:08 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-17 17:08 | +15 | BTC | DOWN | 0.63 | yes | -6.47 |
| 10-17 17:08 | +10 | BTC | DOWN | 0.63 | yes | -6.47 |
| 10-17 17:08 | +5 | BTC | DOWN | 0.63 | yes | -6.47 |
| 10-17 17:07 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-17 17:05 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-17 17:05 | +20 | ETH | DOWN | 0.60 | yes | -6.17 |
| 10-17 17:05 | +15 | ETH | DOWN | 0.60 | yes | -6.17 |
| 10-17 17:04 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 17:04 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 17:04 | +5 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 17:04 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 10-17 17:04 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-17 17:03 | +10 stop | DOGE | UP | 0.34 | 0.65 | 2.78 |
| 10-17 17:03 | +10 stop | ETH | UP | 0.46 | 0.28 | -2.13 |
