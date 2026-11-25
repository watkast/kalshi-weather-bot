# Range-Scalp Bot

*Updated Wed Nov 25 04:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71436 | 62355 | 9081 (156) | 5 | $-19013.96 | -4.2% |
| **+10¢** | 53280 | 42672 | 10608 (202) | 5 | $-17630.81 | -5.3% |
| **+15¢** | 44622 | 33202 | 11420 (259) | 5 | $-15664.89 | -5.6% |
| **+20¢** | 39725 | 27699 | 12026 (325) | 8 | $-14071.99 | -5.6% |
| **+10¢ (15¢ stop)** | 86966 | 86763 | 203 (123) | 2 | $-31965.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 04:52 | +10 stop | BNB | DOWN | 0.43 | 0.58 | 1.14 |
| 11-25 04:50 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 11-25 04:50 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-25 04:50 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.04 |
| 11-25 04:50 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-25 04:50 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-25 04:50 | +10 stop | ETH | DOWN | 0.57 | 0.33 | -2.74 |
| 11-25 04:49 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-25 04:49 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-25 04:48 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 11-25 04:48 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-25 04:48 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-25 04:48 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 11-25 04:48 | +10 stop | NEAR | DOWN | 0.64 | 0.46 | -2.15 |
| 11-25 04:48 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-25 04:48 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-25 04:48 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-25 04:48 | +10 stop | BNB | UP | 0.49 | 0.62 | 0.95 |
| 11-25 04:48 | +10 stop | BTC | UP | 0.53 | 0.37 | -1.95 |
| 11-25 04:48 | +10 | BTC | UP | 0.53 | open |  |
| 11-25 04:47 | +20 | ETH | UP | 0.69 | open |  |
| 11-25 04:47 | +5 | BTC | UP | 0.65 | open |  |
| 11-25 04:47 | +15 | ETH | UP | 0.62 | open |  |
| 11-25 04:47 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 11-25 04:47 | +10 | ETH | UP | 0.63 | open |  |
| 11-25 04:47 | +5 | ETH | UP | 0.63 | open |  |
| 11-25 04:47 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-25 04:47 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-25 04:47 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-25 04:47 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-25 04:47 | +5 | SOL | DOWN | 0.67 | 0.75 | 0.50 |
| 11-25 04:47 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.13 |
| 11-25 04:47 | +20 | HYPE | UP | 0.63 | open |  |
| 11-25 04:47 | +15 | HYPE | UP | 0.63 | open |  |
| 11-25 04:47 | +10 | HYPE | UP | 0.62 | open |  |
| 11-25 04:47 | +5 | HYPE | UP | 0.65 | open |  |
| 11-25 04:47 | +10 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-25 04:47 | +5 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-25 04:46 | +10 stop | BNB | DOWN | 0.54 | 0.38 | -1.95 |
| 11-25 04:46 | +20 | BNB | DOWN | 0.54 | open |  |
