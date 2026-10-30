# Range-Scalp Bot

*Updated Fri Oct 30 00:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39983 | 34926 | 5057 (51) | 3 | $-10945.20 | -4.3% |
| **+10¢** | 29797 | 23948 | 5849 (74) | 3 | $-9674.19 | -5.2% |
| **+15¢** | 24916 | 18624 | 6292 (101) | 3 | $-8660.22 | -5.5% |
| **+20¢** | 22109 | 15511 | 6598 (130) | 3 | $-7582.78 | -5.5% |
| **+10¢ (15¢ stop)** | 48794 | 48724 | 70 (37) | 0 | $-18437.06 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 00:52 | +10 stop | BTC | UP | 0.61 | 0.73 | 0.89 |
| 10-30 00:50 | +10 stop | ETH | UP | 0.65 | 0.83 | 1.53 |
| 10-30 00:50 | +10 stop | ETH | UP | 0.53 | 0.63 | 0.65 |
| 10-30 00:49 | +10 stop | BNB | UP | 0.60 | 0.72 | 0.88 |
| 10-30 00:49 | +5 | BNB | UP | 0.60 | 0.67 | 0.37 |
| 10-30 00:49 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-30 00:49 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-30 00:49 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-30 00:49 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 10-30 00:48 | +5 | XRP | UP | 0.62 | 0.71 | 0.58 |
| 10-30 00:48 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-30 00:48 | +10 stop | BNB | DOWN | 0.53 | 0.35 | -2.14 |
| 10-30 00:47 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-30 00:47 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-30 00:47 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-30 00:47 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-30 00:47 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-30 00:47 | +10 stop | ZEC | DOWN | 0.64 | 0.49 | -1.85 |
| 10-30 00:47 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-30 00:47 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-30 00:47 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-30 00:47 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-30 00:47 | +5 | HYPE | UP | 0.58 | 0.66 | 0.46 |
| 10-30 00:47 | +5 | DOGE | UP | 0.52 | 0.58 | 0.24 |
| 10-30 00:47 | +10 stop | BTC | DOWN | 0.66 | 0.49 | -2.04 |
| 10-30 00:47 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-30 00:47 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-30 00:47 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-30 00:47 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-30 00:47 | +5 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-30 00:46 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 10-30 00:46 | +20 | BNB | UP | 0.57 | 0.85 | 2.53 |
| 10-30 00:46 | +15 | BNB | UP | 0.57 | 0.72 | 1.17 |
| 10-30 00:46 | +10 | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-30 00:46 | +5 | BNB | UP | 0.57 | 0.64 | 0.35 |
| 10-30 00:46 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-30 00:46 | +20 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 10-30 00:46 | +15 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 10-30 00:46 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-30 00:46 | +5 | NEAR | UP | 0.61 | 0.69 | 0.48 |
