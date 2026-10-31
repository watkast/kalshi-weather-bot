# Range-Scalp Bot

*Updated Sat Oct 31 22:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42852 | 37365 | 5487 (62) | 2 | $-12092.51 | -4.5% |
| **+10¢** | 31953 | 25605 | 6348 (84) | 0 | $-10862.46 | -5.4% |
| **+15¢** | 26734 | 19891 | 6843 (112) | 0 | $-9939.64 | -5.9% |
| **+20¢** | 23743 | 16571 | 7172 (145) | 0 | $-8803.37 | -5.9% |
| **+10¢ (15¢ stop)** | 52273 | 52190 | 83 (48) | 0 | $-19803.28 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 22:49 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-31 22:49 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 22:49 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 22:48 | +10 stop | ZEC | DOWN | 0.70 | 0.95 | 2.29 |
| 10-31 22:48 | +20 | ZEC | DOWN | 0.70 | 0.95 | 2.29 |
| 10-31 22:48 | +15 | ZEC | DOWN | 0.70 | 0.95 | 2.29 |
| 10-31 22:48 | +10 | ZEC | DOWN | 0.70 | 0.95 | 2.29 |
| 10-31 22:48 | +5 | ZEC | DOWN | 0.70 | 0.95 | 2.29 |
| 10-31 22:48 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 10-31 22:48 | +5 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 10-31 22:47 | +10 stop | HYPE | UP | 0.57 | 0.37 | -2.35 |
| 10-31 22:47 | +10 stop | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 10-31 22:47 | +5 | HYPE | UP | 0.57 | open |  |
| 10-31 22:47 | +10 stop | NEAR | UP | 0.54 | 0.36 | -2.15 |
| 10-31 22:47 | +10 stop | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-31 22:47 | +20 | BTC | DOWN | 0.71 | 0.94 | 2.05 |
| 10-31 22:47 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-31 22:47 | +10 | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-31 22:47 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-31 22:46 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 10-31 22:46 | +5 | HYPE | UP | 0.58 | 0.66 | 0.46 |
| 10-31 22:46 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-31 22:46 | +20 | SOL | DOWN | 0.66 | 0.88 | 1.96 |
| 10-31 22:46 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-31 22:46 | +10 | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-31 22:46 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 10-31 22:46 | +5 | NEAR | UP | 0.69 | open |  |
| 10-31 22:46 | +10 stop | HYPE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-31 22:46 | +20 | HYPE | DOWN | 0.62 | 0.85 | 2.04 |
| 10-31 22:46 | +15 | HYPE | DOWN | 0.62 | 0.85 | 2.04 |
| 10-31 22:46 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 22:46 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-31 22:46 | +10 stop | NEAR | DOWN | 0.47 | 0.31 | -1.93 |
| 10-31 22:46 | +20 | NEAR | DOWN | 0.47 | 0.71 | 2.07 |
| 10-31 22:46 | +15 | NEAR | DOWN | 0.47 | 0.66 | 1.56 |
| 10-31 22:46 | +10 | NEAR | DOWN | 0.47 | 0.60 | 0.95 |
| 10-31 22:46 | +5 | NEAR | DOWN | 0.47 | 0.54 | 0.34 |
| 10-31 22:46 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-31 22:46 | +20 | ETH | DOWN | 0.62 | 0.88 | 2.35 |
| 10-31 22:46 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
