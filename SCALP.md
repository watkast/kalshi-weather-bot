# Range-Scalp Bot

*Updated Mon Oct 12 01:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12879 | 11120 | 1759 (25) | 4 | $-4235.57 | -5.2% |
| **+10¢** | 9759 | 7725 | 2034 (37) | 5 | $-3966.73 | -6.5% |
| **+15¢** | 8208 | 6040 | 2168 (55) | 6 | $-3454.90 | -6.7% |
| **+20¢** | 7311 | 5052 | 2259 (69) | 5 | $-2946.43 | -6.4% |
| **+10¢ (15¢ stop)** | 15879 | 15838 | 41 (25) | 2 | $-6238.08 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 01:56 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-12 01:56 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-12 01:56 | +10 stop | SOL | DOWN | 0.68 | 0.39 | -3.23 |
| 10-12 01:56 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-12 01:56 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-12 01:56 | +10 | SOL | DOWN | 0.67 | open |  |
| 10-12 01:56 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-12 01:56 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 10-12 01:56 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-12 01:56 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-12 01:56 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-12 01:56 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-12 01:56 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-12 01:55 | +10 stop | DOGE | DOWN | 0.71 | 0.49 | -2.53 |
| 10-12 01:55 | +10 stop | HYPE | UP | 0.56 | 0.68 | 0.86 |
| 10-12 01:55 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-12 01:55 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-12 01:55 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-12 01:55 | +10 | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-12 01:55 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.56 |
| 10-12 01:53 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-12 01:53 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-12 01:53 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 01:53 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-12 01:53 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 01:53 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.48 |
| 10-12 01:52 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-12 01:52 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-12 01:50 | +15 | HYPE | DOWN | 0.71 | open |  |
| 10-12 01:50 | +10 | HYPE | DOWN | 0.71 | open |  |
| 10-12 01:50 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 01:50 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-12 01:49 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-12 01:49 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 01:49 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-12 01:49 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-12 01:49 | +10 stop | HYPE | DOWN | 0.71 | 0.38 | -3.62 |
| 10-12 01:48 | +10 stop | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 10-12 01:47 | +10 stop | HYPE | UP | 0.65 | 0.43 | -2.54 |
| 10-12 01:47 | +10 stop | ETH | UP | 0.63 | 0.39 | -2.74 |
