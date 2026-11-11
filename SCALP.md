# Range-Scalp Bot

*Updated Wed Nov 11 05:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55457 | 48365 | 7092 (94) | 0 | $-15147.40 | -4.3% |
| **+10¢** | 41432 | 33158 | 8274 (124) | 1 | $-14085.42 | -5.4% |
| **+15¢** | 34737 | 25815 | 8922 (158) | 3 | $-12852.33 | -5.9% |
| **+20¢** | 30930 | 21573 | 9357 (207) | 6 | $-11231.40 | -5.8% |
| **+10¢ (15¢ stop)** | 67532 | 67414 | 118 (73) | 0 | $-24863.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 05:17 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-11 05:17 | +20 | ETH | UP | 0.70 | open |  |
| 11-11 05:17 | +15 | ETH | UP | 0.70 | open |  |
| 11-11 05:17 | +10 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-11 05:17 | +5 | ETH | UP | 0.70 | 0.79 | 0.63 |
| 11-11 05:17 | +10 stop | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-11 05:17 | +20 | BNB | UP | 0.62 | open |  |
| 11-11 05:17 | +15 | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-11 05:17 | +10 | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-11 05:17 | +5 | BNB | UP | 0.61 | 0.68 | 0.38 |
| 11-11 05:17 | +10 stop | XRP | UP | 0.67 | 0.83 | 1.34 |
| 11-11 05:17 | +20 | XRP | UP | 0.67 | open |  |
| 11-11 05:17 | +15 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 11-11 05:17 | +10 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 11-11 05:17 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
| 11-11 05:17 | +10 stop | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 05:17 | +20 | ZEC | UP | 0.60 | open |  |
| 11-11 05:17 | +15 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 05:17 | +10 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 05:17 | +5 | ZEC | UP | 0.61 | 0.75 | 1.09 |
| 11-11 05:17 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-11 05:17 | +20 | BTC | UP | 0.64 | open |  |
| 11-11 05:17 | +15 | BTC | UP | 0.64 | open |  |
| 11-11 05:17 | +10 | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-11 05:17 | +5 | BTC | UP | 0.63 | 0.76 | 1.00 |
| 11-11 05:16 | +10 stop | HYPE | UP | 0.70 | 0.55 | -1.83 |
| 11-11 05:16 | +20 | HYPE | UP | 0.70 | open |  |
| 11-11 05:16 | +15 | HYPE | UP | 0.70 | open |  |
| 11-11 05:16 | +10 | HYPE | UP | 0.70 | open |  |
| 11-11 05:16 | +5 | HYPE | UP | 0.70 | 0.77 | 0.42 |
| 11-11 05:16 | +10 stop | NEAR | UP | 0.59 | 0.81 | 1.92 |
| 11-11 05:16 | +20 | NEAR | UP | 0.59 | 0.81 | 1.92 |
| 11-11 05:16 | +15 | NEAR | UP | 0.59 | 0.81 | 1.92 |
| 11-11 05:16 | +10 | NEAR | UP | 0.59 | 0.81 | 1.92 |
| 11-11 05:16 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 11-11 05:16 | +10 stop | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-11 05:16 | +20 | DOGE | UP | 0.56 | 0.77 | 1.79 |
| 11-11 05:16 | +15 | DOGE | UP | 0.56 | 0.77 | 1.79 |
| 11-11 05:16 | +10 | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-11 05:16 | +5 | DOGE | UP | 0.56 | 0.67 | 0.76 |
