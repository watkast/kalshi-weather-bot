# Range-Scalp Bot

*Updated Wed Nov 04 05:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46851 | 40805 | 6046 (72) | 4 | $-13427.40 | -4.6% |
| **+10¢** | 34997 | 27988 | 7009 (96) | 5 | $-12242.47 | -5.6% |
| **+15¢** | 29304 | 21761 | 7543 (124) | 5 | $-11191.37 | -6.1% |
| **+20¢** | 26033 | 18132 | 7901 (164) | 7 | $-9847.78 | -6.0% |
| **+10¢ (15¢ stop)** | 57109 | 57016 | 93 (56) | 4 | $-21313.34 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 05:07 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 11-04 05:07 | +5 | NEAR | DOWN | 0.57 | open |  |
| 11-04 05:07 | +10 stop | ZEC | UP | 0.68 | open |  |
| 11-04 05:07 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-04 05:06 | +10 stop | HYPE | UP | 0.69 | 0.82 | 1.00 |
| 11-04 05:06 | +10 stop | ETH | UP | 0.51 | open |  |
| 11-04 05:06 | +10 stop | NEAR | UP | 0.56 | 0.32 | -2.74 |
| 11-04 05:05 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 05:05 | +10 stop | ETH | UP | 0.71 | 0.54 | -2.03 |
| 11-04 05:04 | +10 stop | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-04 05:04 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-04 05:04 | +5 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 05:04 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.56 |
| 11-04 05:04 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-04 05:04 | +10 | BTC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 05:04 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-04 05:04 | +5 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-04 05:04 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-04 05:04 | +10 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-04 05:04 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 11-04 05:04 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 05:04 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-04 05:04 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 11-04 05:03 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.80 |
| 11-04 05:03 | +20 | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 11-04 05:03 | +15 | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 11-04 05:03 | +10 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-04 05:03 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.56 |
| 11-04 05:03 | +5 | NEAR | DOWN | 0.55 | 0.64 | 0.55 |
| 11-04 05:03 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-04 05:03 | +10 stop | ETH | DOWN | 0.67 | 0.46 | -2.44 |
| 11-04 05:03 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-04 05:03 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-04 05:03 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-04 05:02 | +10 stop | ZEC | DOWN | 0.53 | 0.37 | -1.92 |
| 11-04 05:02 | +10 | ZEC | DOWN | 0.52 | open |  |
| 11-04 05:02 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 11-04 05:02 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-04 05:02 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.05 |
| 11-04 05:02 | +10 | NEAR | DOWN | 0.59 | open |  |
