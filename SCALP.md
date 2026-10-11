# Range-Scalp Bot

*Updated Sun Oct 11 19:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12416 | 10715 | 1701 (25) | 6 | $-4108.10 | -5.2% |
| **+10¢** | 9427 | 7458 | 1969 (37) | 7 | $-3857.35 | -6.5% |
| **+15¢** | 7937 | 5844 | 2093 (55) | 8 | $-3300.42 | -6.6% |
| **+20¢** | 7073 | 4894 | 2179 (69) | 8 | $-2775.43 | -6.3% |
| **+10¢ (15¢ stop)** | 15302 | 15261 | 41 (25) | 3 | $-6018.81 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 19:54 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 10-11 19:54 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 10-11 19:54 | +5 | NEAR | DOWN | 0.54 | open |  |
| 10-11 19:54 | +10 stop | XRP | UP | 0.68 | 0.45 | -2.64 |
| 10-11 19:53 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 19:53 | +10 stop | NEAR | UP | 0.43 | 0.55 | 0.84 |
| 10-11 19:53 | +5 | NEAR | UP | 0.43 | 0.55 | 0.84 |
| 10-11 19:53 | +10 stop | BNB | DOWN | 0.51 | 0.61 | 0.65 |
| 10-11 19:53 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-11 19:53 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-11 19:53 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-11 19:53 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-11 19:52 | +10 stop | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 10-11 19:52 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 19:52 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 19:52 | +5 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-11 19:52 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-11 19:52 | +20 | XRP | UP | 0.70 | open |  |
| 10-11 19:52 | +15 | XRP | UP | 0.70 | open |  |
| 10-11 19:52 | +10 | XRP | UP | 0.70 | open |  |
| 10-11 19:52 | +5 | XRP | UP | 0.70 | open |  |
| 10-11 19:52 | +5 | NEAR | UP | 0.57 | 0.62 | 0.15 |
| 10-11 19:52 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 19:52 | +5 | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 10-11 19:51 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 10-11 19:51 | +20 | BNB | UP | 0.62 | open |  |
| 10-11 19:51 | +15 | BNB | UP | 0.62 | open |  |
| 10-11 19:51 | +10 | BNB | UP | 0.62 | open |  |
| 10-11 19:51 | +5 | BNB | UP | 0.62 | open |  |
| 10-11 19:51 | +10 stop | ETH | UP | 0.53 | 0.63 | 0.65 |
| 10-11 19:51 | +20 | ETH | UP | 0.53 | open |  |
| 10-11 19:51 | +15 | ETH | UP | 0.53 | open |  |
| 10-11 19:51 | +10 | ETH | UP | 0.53 | 0.63 | 0.65 |
| 10-11 19:51 | +5 | ETH | UP | 0.53 | 0.63 | 0.65 |
| 10-11 19:51 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-11 19:51 | +5 | HYPE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-11 19:50 | +5 | HYPE | UP | 0.54 | 0.59 | 0.15 |
| 10-11 19:49 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.15 |
| 10-11 19:49 | +15 | HYPE | UP | 0.63 | open |  |
| 10-11 19:49 | +10 | HYPE | UP | 0.63 | open |  |
