# Range-Scalp Bot

*Updated Thu Nov 19 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64606 | 56364 | 8242 (124) | 1 | $-17528.57 | -4.3% |
| **+10¢** | 48263 | 38622 | 9641 (165) | 2 | $-16340.07 | -5.4% |
| **+15¢** | 40471 | 30076 | 10395 (210) | 3 | $-14768.74 | -5.8% |
| **+20¢** | 36042 | 25127 | 10915 (265) | 3 | $-13074.66 | -5.8% |
| **+10¢ (15¢ stop)** | 78611 | 78447 | 164 (98) | 0 | $-28883.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 02:26 | +5 | XRP | UP | 0.52 | 0.67 | 1.16 |
| 11-19 02:25 | +10 stop | XRP | UP | 0.64 | 0.77 | 1.00 |
| 11-19 02:25 | +10 | XRP | UP | 0.64 | 0.77 | 1.00 |
| 11-19 02:25 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 11-19 02:25 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-19 02:25 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-19 02:25 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 11-19 02:24 | +15 | XRP | DOWN | 0.45 | open |  |
| 11-19 02:24 | +10 | XRP | DOWN | 0.45 | 0.59 | 1.05 |
| 11-19 02:24 | +10 stop | XRP | DOWN | 0.46 | 0.65 | 1.56 |
| 11-19 02:24 | +5 | XRP | DOWN | 0.46 | 0.65 | 1.56 |
| 11-19 02:24 | +10 stop | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-19 02:24 | +5 | DOGE | UP | 0.50 | 0.57 | 0.34 |
| 11-19 02:23 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-19 02:23 | +10 stop | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 11-19 02:23 | +20 | SOL | DOWN | 0.55 | 0.78 | 1.99 |
| 11-19 02:23 | +15 | SOL | DOWN | 0.55 | 0.72 | 1.37 |
| 11-19 02:23 | +10 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 02:23 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 11-19 02:22 | +10 stop | ZEC | DOWN | 0.55 | 0.86 | 2.83 |
| 11-19 02:22 | +20 | ZEC | DOWN | 0.56 | 0.86 | 2.73 |
| 11-19 02:22 | +15 | ZEC | DOWN | 0.56 | 0.86 | 2.73 |
| 11-19 02:22 | +10 | ZEC | DOWN | 0.56 | 0.86 | 2.73 |
| 11-19 02:22 | +5 | ZEC | DOWN | 0.56 | 0.86 | 2.73 |
| 11-19 02:22 | +10 stop | XRP | DOWN | 0.49 | 0.59 | 0.65 |
| 11-19 02:22 | +15 | XRP | DOWN | 0.50 | 0.65 | 1.16 |
| 11-19 02:22 | +10 | XRP | DOWN | 0.50 | 0.65 | 1.16 |
| 11-19 02:22 | +5 | XRP | DOWN | 0.50 | 0.59 | 0.55 |
| 11-19 02:22 | +10 stop | DOGE | DOWN | 0.46 | 0.67 | 1.76 |
| 11-19 02:22 | +5 | DOGE | DOWN | 0.47 | 0.67 | 1.66 |
| 11-19 02:22 | +10 stop | NEAR | DOWN | 0.59 | 0.36 | -2.64 |
| 11-19 02:22 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-19 02:22 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-19 02:20 | +10 stop | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-19 02:20 | +10 stop | NEAR | DOWN | 0.56 | 0.73 | 1.35 |
| 11-19 02:20 | +10 | NEAR | DOWN | 0.56 | 0.73 | 1.35 |
| 11-19 02:20 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.22 |
| 11-19 02:20 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 11-19 02:17 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-19 02:17 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
