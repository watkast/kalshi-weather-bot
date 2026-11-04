# Range-Scalp Bot

*Updated Wed Nov 04 05:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46860 | 40814 | 6046 (72) | 2 | $-13421.83 | -4.5% |
| **+10¢** | 35006 | 27997 | 7009 (96) | 3 | $-12232.43 | -5.6% |
| **+15¢** | 29310 | 21767 | 7543 (124) | 3 | $-11181.15 | -6.1% |
| **+20¢** | 26040 | 18139 | 7901 (164) | 2 | $-9832.04 | -6.0% |
| **+10¢ (15¢ stop)** | 57125 | 57032 | 93 (56) | 0 | $-21311.50 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 05:12 | +10 stop | BTC | DOWN | 0.56 | 0.85 | 2.63 |
| 11-04 05:12 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-04 05:12 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-04 05:11 | +10 stop | BTC | UP | 0.61 | 0.43 | -2.15 |
| 11-04 05:11 | +15 | BTC | UP | 0.61 | open |  |
| 11-04 05:11 | +10 | BTC | UP | 0.61 | open |  |
| 11-04 05:11 | +5 | BTC | UP | 0.61 | open |  |
| 11-04 05:11 | +10 stop | DOGE | UP | 0.27 | 0.68 | 3.80 |
| 11-04 05:10 | +10 stop | SOL | DOWN | 0.45 | 0.25 | -2.32 |
| 11-04 05:10 | +10 | SOL | DOWN | 0.45 | 0.62 | 1.35 |
| 11-04 05:10 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 11-04 05:09 | +10 stop | DOGE | DOWN | 0.71 | 0.44 | -3.03 |
| 11-04 05:09 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.95 |
| 11-04 05:09 | +15 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-04 05:09 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 05:09 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 05:09 | +10 stop | NEAR | UP | 0.60 | 0.89 | 2.66 |
| 11-04 05:09 | +10 stop | ETH | UP | 0.63 | 0.78 | 1.20 |
| 11-04 05:09 | +10 stop | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 11-04 05:09 | +20 | SOL | DOWN | 0.53 | 0.73 | 1.68 |
| 11-04 05:09 | +15 | SOL | DOWN | 0.53 | 0.73 | 1.68 |
| 11-04 05:09 | +10 | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 11-04 05:09 | +5 | SOL | DOWN | 0.53 | 0.61 | 0.45 |
| 11-04 05:09 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-04 05:09 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-04 05:09 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 11-04 05:09 | +10 stop | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 05:09 | +15 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 05:09 | +10 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 05:09 | +5 | BNB | DOWN | 0.58 | 0.63 | 0.15 |
| 11-04 05:09 | +5 | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 11-04 05:09 | +10 stop | ETH | DOWN | 0.59 | 0.39 | -2.34 |
| 11-04 05:07 | +10 stop | NEAR | DOWN | 0.57 | 0.35 | -2.54 |
| 11-04 05:07 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.46 |
| 11-04 05:07 | +10 stop | ZEC | UP | 0.68 | 0.80 | 0.92 |
| 11-04 05:07 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-04 05:06 | +10 stop | HYPE | UP | 0.69 | 0.82 | 1.00 |
| 11-04 05:06 | +10 stop | ETH | UP | 0.51 | 0.35 | -1.94 |
| 11-04 05:06 | +10 stop | NEAR | UP | 0.56 | 0.32 | -2.74 |
| 11-04 05:05 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
