# Range-Scalp Bot

*Updated Fri Oct 09 11:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9012 | 7788 | 1224 (14) | 1 | $-3003.37 | -5.3% |
| **+10¢** | 6821 | 5389 | 1432 (26) | 2 | $-2860.53 | -6.7% |
| **+15¢** | 5752 | 4243 | 1509 (38) | 3 | $-2337.64 | -6.5% |
| **+20¢** | 5118 | 3552 | 1566 (46) | 6 | $-1939.35 | -6.0% |
| **+10¢ (15¢ stop)** | 10995 | 10965 | 30 (19) | 0 | $-4144.04 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 11:33 | +10 stop | BNB | UP | 0.45 | 0.68 | 1.96 |
| 10-09 11:33 | +10 | BNB | UP | 0.45 | 0.68 | 1.96 |
| 10-09 11:33 | +5 | BNB | UP | 0.45 | 0.68 | 1.96 |
| 10-09 11:32 | +10 stop | HYPE | UP | 0.57 | 0.41 | -1.95 |
| 10-09 11:32 | +20 | HYPE | UP | 0.57 | open |  |
| 10-09 11:32 | +15 | HYPE | UP | 0.57 | open |  |
| 10-09 11:32 | +10 | HYPE | UP | 0.57 | open |  |
| 10-09 11:32 | +5 | HYPE | UP | 0.57 | open |  |
| 10-09 11:31 | +10 stop | XRP | UP | 0.62 | 0.80 | 1.51 |
| 10-09 11:31 | +20 | XRP | UP | 0.62 | open |  |
| 10-09 11:31 | +15 | XRP | UP | 0.62 | 0.80 | 1.51 |
| 10-09 11:31 | +10 | XRP | UP | 0.62 | 0.80 | 1.51 |
| 10-09 11:31 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 10-09 11:31 | +10 stop | DOGE | UP | 0.71 | 0.88 | 1.49 |
| 10-09 11:31 | +20 | DOGE | UP | 0.71 | open |  |
| 10-09 11:31 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-09 11:31 | +10 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-09 11:31 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 10-09 11:31 | +10 stop | BNB | DOWN | 0.48 | 0.62 | 1.05 |
| 10-09 11:31 | +20 | BNB | DOWN | 0.48 | open |  |
| 10-09 11:31 | +15 | BNB | DOWN | 0.48 | open |  |
| 10-09 11:31 | +10 | BNB | DOWN | 0.48 | 0.62 | 1.05 |
| 10-09 11:31 | +5 | BNB | DOWN | 0.48 | 0.62 | 1.05 |
| 10-09 11:31 | +10 stop | ZEC | DOWN | 0.60 | 0.20 | -4.29 |
| 10-09 11:31 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-09 11:31 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-09 11:31 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-09 11:31 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-09 11:31 | +10 stop | NEAR | UP | 0.70 | 0.89 | 1.69 |
| 10-09 11:31 | +20 | NEAR | UP | 0.70 | open |  |
| 10-09 11:31 | +15 | NEAR | UP | 0.70 | 0.89 | 1.69 |
| 10-09 11:31 | +10 | NEAR | UP | 0.70 | 0.89 | 1.69 |
| 10-09 11:31 | +5 | NEAR | UP | 0.70 | 0.89 | 1.69 |
| 10-09 11:27 | +10 stop | ETH | DOWN | 0.38 | 0.53 | 1.15 |
| 10-09 11:26 | +10 stop | BTC | UP | 0.62 | 0.79 | 1.41 |
| 10-09 11:26 | +10 | BTC | UP | 0.62 | 0.79 | 1.41 |
| 10-09 11:26 | +5 | BTC | UP | 0.62 | 0.68 | 0.27 |
| 10-09 11:26 | +10 stop | ETH | UP | 0.59 | 0.40 | -2.24 |
| 10-09 11:26 | +10 stop | XRP | DOWN | 0.67 | 0.22 | -4.78 |
| 10-09 11:26 | +10 stop | ETH | UP | 0.48 | 0.62 | 1.05 |
