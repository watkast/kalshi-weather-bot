# Range-Scalp Bot

*Updated Sun Nov 01 11:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43541 | 37939 | 5602 (63) | 4 | $-12446.28 | -4.5% |
| **+10¢** | 32482 | 26012 | 6470 (85) | 4 | $-11161.45 | -5.5% |
| **+15¢** | 27188 | 20221 | 6967 (112) | 5 | $-10185.47 | -6.0% |
| **+20¢** | 24143 | 16846 | 7297 (146) | 6 | $-8990.82 | -5.9% |
| **+10¢ (15¢ stop)** | 53130 | 53045 | 85 (50) | 0 | $-20101.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 11:24 | +10 stop | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-01 11:24 | +15 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-01 11:24 | +10 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-01 11:24 | +5 | ZEC | UP | 0.62 | 0.70 | 0.48 |
| 11-01 11:24 | +10 stop | XRP | UP | 0.53 | 0.84 | 2.82 |
| 11-01 11:23 | +10 stop | HYPE | UP | 0.61 | 0.41 | -2.34 |
| 11-01 11:23 | +5 | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-01 11:23 | +10 stop | BNB | UP | 0.50 | 0.27 | -2.62 |
| 11-01 11:22 | +5 | HYPE | DOWN | 0.49 | 0.54 | 0.14 |
| 11-01 11:22 | +10 stop | BTC | UP | 0.57 | 0.69 | 0.87 |
| 11-01 11:22 | +10 stop | XRP | DOWN | 0.57 | 0.40 | -2.05 |
| 11-01 11:22 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.05 |
| 11-01 11:21 | +10 stop | NEAR | UP | 0.63 | 0.84 | 1.83 |
| 11-01 11:20 | +5 | BNB | UP | 0.55 | open |  |
| 11-01 11:19 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-01 11:19 | +10 stop | XRP | DOWN | 0.52 | 0.65 | 0.96 |
| 11-01 11:18 | +10 stop | DOGE | UP | 0.56 | 0.26 | -3.32 |
| 11-01 11:18 | +5 | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 11-01 11:18 | +5 | SOL | DOWN | 0.63 | 0.72 | 0.58 |
| 11-01 11:18 | +5 | NEAR | DOWN | 0.61 | open |  |
| 11-01 11:18 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 11:18 | +10 stop | ZEC | UP | 0.54 | 0.72 | 1.47 |
| 11-01 11:18 | +15 | ZEC | UP | 0.54 | 0.72 | 1.47 |
| 11-01 11:18 | +10 | ZEC | UP | 0.54 | 0.72 | 1.47 |
| 11-01 11:18 | +5 | ZEC | UP | 0.54 | 0.60 | 0.25 |
| 11-01 11:17 | +10 stop | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-01 11:17 | +20 | ZEC | DOWN | 0.38 | open |  |
| 11-01 11:17 | +15 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-01 11:17 | +10 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-01 11:17 | +5 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-01 11:17 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 11:17 | +20 | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 11-01 11:17 | +15 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-01 11:17 | +10 | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 11:17 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
| 11-01 11:16 | +10 stop | HYPE | DOWN | 0.71 | 0.54 | -2.03 |
| 11-01 11:16 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-01 11:16 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-01 11:16 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-01 11:16 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
