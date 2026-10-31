# Range-Scalp Bot

*Updated Sat Oct 31 19:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42645 | 37182 | 5463 (61) | 0 | $-12077.03 | -4.5% |
| **+10¢** | 31802 | 25480 | 6322 (83) | 0 | $-10864.56 | -5.4% |
| **+15¢** | 26600 | 19782 | 6818 (111) | 1 | $-9977.69 | -6.0% |
| **+20¢** | 23626 | 16481 | 7145 (143) | 1 | $-8852.42 | -6.0% |
| **+10¢ (15¢ stop)** | 52029 | 51946 | 83 (48) | 0 | $-19678.33 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 19:27 | +10 stop | HYPE | DOWN | 0.39 | 0.54 | 1.15 |
| 10-31 19:27 | +10 | HYPE | DOWN | 0.39 | 0.54 | 1.15 |
| 10-31 19:27 | +5 | HYPE | DOWN | 0.39 | 0.54 | 1.15 |
| 10-31 19:26 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.87 |
| 10-31 19:26 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-31 19:26 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-31 19:26 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.77 |
| 10-31 19:26 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-31 19:16 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +20 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 10-31 19:16 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +10 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-31 19:16 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-31 19:16 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-31 19:16 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 19:16 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-31 19:16 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 10-31 19:16 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 19:16 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-31 19:16 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:16 | +20 | BTC | DOWN | 0.68 | 0.91 | 2.04 |
| 10-31 19:16 | +15 | BTC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-31 19:16 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:16 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:08 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-31 19:08 | +10 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-31 19:08 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-31 19:08 | +20 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-31 19:04 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.74 |
| 10-31 19:04 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-31 19:04 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:04 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-31 19:04 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-31 19:04 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-31 19:04 | +10 stop | HYPE | UP | 0.62 | 0.18 | -4.68 |
| 10-31 19:03 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
