# Range-Scalp Bot

*Updated Thu Nov 05 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48868 | 42585 | 6283 (74) | 3 | $-13871.95 | -4.5% |
| **+10¢** | 36478 | 29173 | 7305 (100) | 3 | $-12747.94 | -5.6% |
| **+15¢** | 30553 | 22685 | 7868 (129) | 4 | $-11639.31 | -6.1% |
| **+20¢** | 27148 | 18902 | 8246 (168) | 4 | $-10306.97 | -6.1% |
| **+10¢ (15¢ stop)** | 59558 | 59463 | 95 (57) | 0 | $-22042.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 23:23 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-05 23:22 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 11-05 23:22 | +10 | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-05 23:22 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-05 23:22 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-05 23:21 | +10 stop | ZEC | UP | 0.65 | 0.81 | 1.35 |
| 11-05 23:21 | +10 | ZEC | UP | 0.65 | 0.81 | 1.35 |
| 11-05 23:21 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 11-05 23:21 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-05 23:21 | +10 stop | ZEC | DOWN | 0.41 | 0.54 | 0.95 |
| 11-05 23:21 | +15 | ZEC | DOWN | 0.41 | open |  |
| 11-05 23:21 | +10 | ZEC | DOWN | 0.41 | 0.54 | 0.91 |
| 11-05 23:21 | +5 | ZEC | DOWN | 0.41 | 0.54 | 0.91 |
| 11-05 23:21 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-05 23:21 | +10 stop | SOL | DOWN | 0.64 | 0.42 | -2.55 |
| 11-05 23:21 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-05 23:21 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-05 23:21 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-05 23:20 | +10 stop | HYPE | DOWN | 0.55 | 0.26 | -3.22 |
| 11-05 23:20 | +10 stop | BNB | DOWN | 0.59 | 0.42 | -2.05 |
| 11-05 23:20 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-05 23:20 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-05 23:20 | +10 | BNB | DOWN | 0.60 | open |  |
| 11-05 23:20 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-05 23:19 | +10 stop | BTC | DOWN | 0.55 | 0.32 | -2.64 |
| 11-05 23:19 | +10 stop | ETH | DOWN | 0.55 | 0.35 | -2.34 |
| 11-05 23:19 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 11-05 23:19 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-05 23:19 | +10 stop | DOGE | UP | 0.42 | 0.54 | 0.84 |
| 11-05 23:18 | +5 | BTC | UP | 0.65 | 0.72 | 0.39 |
| 11-05 23:18 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-05 23:18 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-05 23:18 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-05 23:18 | +10 | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-05 23:18 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-05 23:18 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-05 23:18 | +5 | XRP | DOWN | 0.54 | 0.60 | 0.25 |
| 11-05 23:18 | +5 | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 11-05 23:18 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-05 23:18 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
