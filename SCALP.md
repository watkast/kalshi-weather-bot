# Range-Scalp Bot

*Updated Sun Oct 25 17:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33501 | 29234 | 4267 (42) | 3 | $-9382.38 | -4.4% |
| **+10¢** | 25074 | 20137 | 4937 (60) | 4 | $-8321.95 | -5.3% |
| **+15¢** | 20973 | 15658 | 5315 (83) | 4 | $-7485.66 | -5.7% |
| **+20¢** | 18588 | 13023 | 5565 (105) | 4 | $-6585.97 | -5.6% |
| **+10¢ (15¢ stop)** | 41064 | 41004 | 60 (32) | 4 | $-15659.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 17:51 | +10 stop | BTC | UP | 0.56 | open |  |
| 10-25 17:51 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-25 17:50 | +10 stop | BNB | UP | 0.67 | open |  |
| 10-25 17:49 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-25 17:49 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-25 17:49 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-25 17:49 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-25 17:49 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-25 17:49 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-25 17:48 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 17:48 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 17:48 | +5 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 17:47 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-25 17:47 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-25 17:47 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-25 17:47 | +10 stop | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-25 17:47 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 10-25 17:47 | +15 | NEAR | DOWN | 0.59 | 0.76 | 1.40 |
| 10-25 17:47 | +10 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-25 17:47 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-25 17:47 | +5 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-25 17:47 | +10 stop | BTC | DOWN | 0.57 | 0.41 | -1.95 |
| 10-25 17:47 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-25 17:47 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-25 17:47 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-25 17:47 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-25 17:47 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-25 17:46 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-25 17:46 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-25 17:46 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-25 17:46 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-25 17:46 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-25 17:46 | +10 stop | BNB | DOWN | 0.57 | 0.40 | -2.05 |
| 10-25 17:46 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-25 17:46 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-25 17:46 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-25 17:46 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-25 17:46 | +10 stop | XRP | DOWN | 0.61 | 0.80 | 1.61 |
| 10-25 17:46 | +20 | XRP | DOWN | 0.61 | 0.83 | 1.93 |
| 10-25 17:46 | +15 | XRP | DOWN | 0.61 | 0.80 | 1.61 |
