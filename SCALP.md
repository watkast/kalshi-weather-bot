# Range-Scalp Bot

*Updated Fri Nov 27 17:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73810 | 64416 | 9394 (171) | 6 | $-19619.18 | -4.2% |
| **+10¢** | 55002 | 44030 | 10972 (216) | 6 | $-18251.87 | -5.3% |
| **+15¢** | 46056 | 34238 | 11818 (274) | 7 | $-16345.00 | -5.7% |
| **+20¢** | 40983 | 28534 | 12449 (341) | 8 | $-14785.49 | -5.8% |
| **+10¢ (15¢ stop)** | 89876 | 89657 | 219 (135) | 6 | $-33216.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 17:18 | +5 | DOGE | DOWN | 0.61 | open |  |
| 11-27 17:18 | +10 stop | SOL | DOWN | 0.57 | open |  |
| 11-27 17:18 | +10 stop | XRP | DOWN | 0.55 | open |  |
| 11-27 17:17 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-27 17:17 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-27 17:17 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 11-27 17:17 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-27 17:17 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-27 17:17 | +10 | DOGE | DOWN | 0.61 | open |  |
| 11-27 17:17 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.40 |
| 11-27 17:17 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 11-27 17:17 | +20 | ETH | DOWN | 0.66 | open |  |
| 11-27 17:17 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-27 17:17 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-27 17:17 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-27 17:17 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-27 17:17 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-27 17:17 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 11-27 17:17 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-27 17:17 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-27 17:17 | +10 | BNB | DOWN | 0.63 | open |  |
| 11-27 17:17 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-27 17:16 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 11-27 17:16 | +20 | SOL | UP | 0.55 | open |  |
| 11-27 17:16 | +15 | SOL | UP | 0.55 | open |  |
| 11-27 17:16 | +10 | SOL | UP | 0.55 | open |  |
| 11-27 17:16 | +5 | SOL | UP | 0.55 | open |  |
| 11-27 17:16 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-27 17:16 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-27 17:16 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-27 17:16 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-27 17:16 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 11-27 17:16 | +10 stop | ZEC | DOWN | 0.53 | 0.63 | 0.65 |
| 11-27 17:16 | +20 | ZEC | DOWN | 0.53 | 0.73 | 1.68 |
| 11-27 17:16 | +15 | ZEC | DOWN | 0.53 | 0.69 | 1.27 |
| 11-27 17:16 | +10 | ZEC | DOWN | 0.53 | 0.63 | 0.65 |
| 11-27 17:16 | +5 | ZEC | DOWN | 0.53 | 0.62 | 0.55 |
| 11-27 17:16 | +10 stop | BTC | DOWN | 0.53 | 0.63 | 0.65 |
| 11-27 17:16 | +20 | BTC | DOWN | 0.53 | open |  |
| 11-27 17:16 | +15 | BTC | DOWN | 0.53 | 0.70 | 1.37 |
