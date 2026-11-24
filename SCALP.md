# Range-Scalp Bot

*Updated Tue Nov 24 23:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71277 | 62216 | 9061 (156) | 3 | $-18980.74 | -4.2% |
| **+10¢** | 53162 | 42579 | 10583 (202) | 6 | $-17578.77 | -5.3% |
| **+15¢** | 44524 | 33131 | 11393 (259) | 8 | $-15616.02 | -5.6% |
| **+20¢** | 39642 | 27646 | 11996 (325) | 8 | $-13998.39 | -5.6% |
| **+10¢ (15¢ stop)** | 86774 | 86573 | 201 (121) | 6 | $-31901.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 23:50 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-24 23:50 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-24 23:50 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-24 23:50 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 11-24 23:50 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-24 23:50 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-24 23:50 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-24 23:50 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-24 23:49 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-24 23:49 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-24 23:49 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-24 23:49 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-24 23:49 | +5 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-24 23:49 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-24 23:49 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-24 23:49 | +10 stop | ZEC | UP | 0.53 | open |  |
| 11-24 23:49 | +10 | ZEC | UP | 0.51 | open |  |
| 11-24 23:49 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
| 11-24 23:48 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-24 23:48 | +5 | BTC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-24 23:48 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-24 23:47 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-24 23:47 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 23:47 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 23:47 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-24 23:47 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 11-24 23:47 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-24 23:47 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-24 23:47 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-24 23:47 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 11-24 23:47 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-24 23:47 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-24 23:47 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-24 23:47 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-24 23:47 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-24 23:47 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-24 23:47 | +10 stop | ZEC | UP | 0.59 | 0.69 | 0.68 |
| 11-24 23:47 | +20 | ZEC | UP | 0.58 | open |  |
| 11-24 23:47 | +15 | ZEC | UP | 0.58 | open |  |
| 11-24 23:47 | +10 | ZEC | UP | 0.59 | 0.69 | 0.68 |
