# Range-Scalp Bot

*Updated Thu Nov 12 04:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56607 | 49347 | 7260 (98) | 4 | $-15596.41 | -4.4% |
| **+10¢** | 42299 | 33830 | 8469 (128) | 3 | $-14546.86 | -5.5% |
| **+15¢** | 35465 | 26347 | 9118 (162) | 5 | $-13186.73 | -5.9% |
| **+20¢** | 31597 | 22028 | 9569 (212) | 6 | $-11577.44 | -5.8% |
| **+10¢ (15¢ stop)** | 69003 | 68880 | 123 (73) | 3 | $-25484.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 04:05 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-12 04:05 | +10 stop | DOGE | UP | 0.61 | open |  |
| 11-12 04:03 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-12 04:03 | +5 | ZEC | UP | 0.59 | 0.66 | 0.37 |
| 11-12 04:03 | +10 stop | ZEC | UP | 0.57 | 0.76 | 1.59 |
| 11-12 04:03 | +20 | ZEC | UP | 0.56 | 0.76 | 1.69 |
| 11-12 04:03 | +15 | ZEC | UP | 0.56 | 0.76 | 1.69 |
| 11-12 04:03 | +10 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-12 04:03 | +5 | ZEC | UP | 0.56 | 0.61 | 0.15 |
| 11-12 04:03 | +5 | BNB | UP | 0.68 | 0.76 | 0.52 |
| 11-12 04:02 | +10 stop | SOL | UP | 0.56 | open |  |
| 11-12 04:02 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-12 04:02 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-12 04:02 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 04:02 | +10 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-12 04:02 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 11-12 04:02 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-12 04:02 | +20 | BNB | UP | 0.64 | open |  |
| 11-12 04:02 | +15 | BNB | UP | 0.64 | open |  |
| 11-12 04:02 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-12 04:02 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-12 04:02 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.89 |
| 11-12 04:02 | +20 | DOGE | UP | 0.58 | open |  |
| 11-12 04:02 | +15 | DOGE | UP | 0.58 | open |  |
| 11-12 04:02 | +10 | DOGE | UP | 0.58 | open |  |
| 11-12 04:02 | +5 | DOGE | UP | 0.58 | open |  |
| 11-12 04:01 | +10 stop | SOL | UP | 0.70 | 0.51 | -2.23 |
| 11-12 04:01 | +20 | SOL | UP | 0.70 | open |  |
| 11-12 04:01 | +15 | SOL | UP | 0.70 | open |  |
| 11-12 04:01 | +10 | SOL | UP | 0.70 | open |  |
| 11-12 04:01 | +5 | SOL | UP | 0.70 | open |  |
| 11-12 04:01 | +10 stop | ETH | UP | 0.66 | 0.50 | -1.94 |
| 11-12 04:01 | +20 | ETH | UP | 0.66 | open |  |
| 11-12 04:01 | +15 | ETH | UP | 0.66 | open |  |
| 11-12 04:01 | +10 | ETH | UP | 0.66 | open |  |
| 11-12 04:01 | +5 | ETH | UP | 0.66 | open |  |
| 11-12 04:01 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-12 04:01 | +20 | BTC | UP | 0.69 | open |  |
| 11-12 04:01 | +15 | BTC | UP | 0.69 | open |  |
| 11-12 04:01 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
