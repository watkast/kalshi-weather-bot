# Range-Scalp Bot

*Updated Sun Oct 11 00:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11128 | 9595 | 1533 (22) | 3 | $-3770.81 | -5.4% |
| **+10¢** | 8429 | 6644 | 1785 (36) | 5 | $-3600.41 | -6.8% |
| **+15¢** | 7102 | 5214 | 1888 (52) | 6 | $-3045.94 | -6.8% |
| **+20¢** | 6323 | 4358 | 1965 (66) | 7 | $-2565.32 | -6.5% |
| **+10¢ (15¢ stop)** | 13715 | 13674 | 41 (25) | 3 | $-5500.30 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 00:19 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-11 00:19 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-11 00:19 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-11 00:19 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-11 00:19 | +5 | XRP | DOWN | 0.67 | 0.76 | 0.60 |
| 10-11 00:19 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-11 00:19 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 10-11 00:18 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-11 00:18 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-11 00:18 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 10-11 00:18 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 10-11 00:17 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.72 |
| 10-11 00:17 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-11 00:17 | +15 | ZEC | DOWN | 0.68 | open |  |
| 10-11 00:17 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.74 |
| 10-11 00:17 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.41 |
| 10-11 00:16 | +10 stop | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-11 00:16 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-11 00:16 | +15 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-11 00:16 | +10 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-11 00:16 | +5 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-11 00:16 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 00:16 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-11 00:16 | +15 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 10-11 00:16 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 00:16 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 00:16 | +10 stop | NEAR | UP | 0.62 | 0.42 | -2.34 |
| 10-11 00:16 | +20 | NEAR | UP | 0.62 | open |  |
| 10-11 00:16 | +15 | NEAR | UP | 0.62 | open |  |
| 10-11 00:16 | +10 | NEAR | UP | 0.62 | open |  |
| 10-11 00:16 | +5 | NEAR | UP | 0.62 | open |  |
| 10-11 00:16 | +10 stop | HYPE | DOWN | 0.69 | 0.45 | -2.71 |
| 10-11 00:16 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-11 00:16 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-11 00:16 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-11 00:16 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-11 00:16 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 1.01 |
| 10-11 00:16 | +20 | SOL | DOWN | 0.62 | open |  |
| 10-11 00:16 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-11 00:16 | +10 | SOL | DOWN | 0.62 | 0.75 | 1.01 |
