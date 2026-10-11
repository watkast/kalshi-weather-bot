# Range-Scalp Bot

*Updated Sun Oct 11 16:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12179 | 10503 | 1676 (24) | 4 | $-4081.70 | -5.3% |
| **+10¢** | 9253 | 7309 | 1944 (37) | 4 | $-3855.43 | -6.6% |
| **+15¢** | 7799 | 5736 | 2063 (54) | 5 | $-3291.05 | -6.7% |
| **+20¢** | 6948 | 4799 | 2149 (68) | 6 | $-2789.39 | -6.4% |
| **+10¢ (15¢ stop)** | 15002 | 14961 | 41 (25) | 4 | $-5925.36 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 16:34 | +15 | HYPE | UP | 0.67 | open |  |
| 10-11 16:34 | +5 | HYPE | UP | 0.67 | open |  |
| 10-11 16:34 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 10-11 16:34 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-11 16:34 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-11 16:34 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-11 16:34 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-11 16:33 | +5 | NEAR | UP | 0.69 | open |  |
| 10-11 16:33 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-11 16:33 | +10 | HYPE | UP | 0.70 | open |  |
| 10-11 16:32 | +5 | HYPE | UP | 0.67 | 0.73 | 0.26 |
| 10-11 16:32 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-11 16:32 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-11 16:31 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-11 16:31 | +20 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 16:31 | +15 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 16:31 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-11 16:31 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 16:31 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 16:31 | +20 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-11 16:31 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 10-11 16:31 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 16:31 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-11 16:31 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-11 16:31 | +20 | NEAR | UP | 0.63 | open |  |
| 10-11 16:31 | +15 | NEAR | UP | 0.63 | open |  |
| 10-11 16:31 | +10 | NEAR | UP | 0.63 | open |  |
| 10-11 16:31 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-11 16:31 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-11 16:31 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-11 16:31 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-11 16:31 | +10 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-11 16:31 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-11 16:31 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-11 16:31 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-11 16:31 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-11 16:31 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-11 16:31 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 16:31 | +10 stop | BNB | UP | 0.57 | 0.37 | -2.35 |
| 10-11 16:31 | +20 | BNB | UP | 0.57 | open |  |
