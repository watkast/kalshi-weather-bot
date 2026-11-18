# Range-Scalp Bot

*Updated Wed Nov 18 04:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63618 | 55485 | 8133 (118) | 4 | $-17388.43 | -4.3% |
| **+10¢** | 47525 | 38005 | 9520 (159) | 5 | $-16317.70 | -5.5% |
| **+15¢** | 39851 | 29586 | 10265 (204) | 5 | $-14790.23 | -5.9% |
| **+20¢** | 35494 | 24721 | 10773 (259) | 5 | $-13060.40 | -5.9% |
| **+10¢ (15¢ stop)** | 77417 | 77259 | 158 (93) | 0 | $-28449.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 04:56 | +10 stop | ZEC | UP | 0.65 | 0.43 | -2.54 |
| 11-18 04:56 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 11-18 04:55 | +5 | HYPE | UP | 0.59 | 0.66 | 0.37 |
| 11-18 04:55 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 11-18 04:55 | +5 | ZEC | UP | 0.66 | open |  |
| 11-18 04:54 | +10 stop | NEAR | UP | 0.65 | 0.84 | 1.64 |
| 11-18 04:54 | +10 stop | HYPE | DOWN | 0.54 | 0.38 | -1.93 |
| 11-18 04:54 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-18 04:54 | +5 | HYPE | DOWN | 0.54 | 0.61 | 0.37 |
| 11-18 04:54 | +5 | ZEC | DOWN | 0.48 | 0.57 | 0.54 |
| 11-18 04:53 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-18 04:53 | +10 stop | HYPE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-18 04:53 | +15 | HYPE | DOWN | 0.52 | open |  |
| 11-18 04:53 | +10 | HYPE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-18 04:53 | +5 | HYPE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-18 04:53 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 11-18 04:53 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-18 04:52 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-18 04:51 | +10 stop | DOGE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-18 04:51 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-18 04:51 | +10 stop | XRP | UP | 0.64 | 0.76 | 0.90 |
| 11-18 04:51 | +20 | XRP | UP | 0.64 | 0.92 | 2.58 |
| 11-18 04:51 | +15 | XRP | UP | 0.64 | 0.83 | 1.63 |
| 11-18 04:51 | +10 | XRP | UP | 0.64 | 0.76 | 0.90 |
| 11-18 04:51 | +5 | XRP | UP | 0.64 | 0.72 | 0.48 |
| 11-18 04:51 | +10 stop | BTC | UP | 0.51 | 0.70 | 1.57 |
| 11-18 04:51 | +10 stop | NEAR | UP | 0.61 | 0.44 | -2.05 |
| 11-18 04:51 | +15 | NEAR | UP | 0.61 | 0.84 | 2.03 |
| 11-18 04:51 | +10 | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 11-18 04:51 | +5 | NEAR | UP | 0.61 | 0.67 | 0.27 |
| 11-18 04:50 | +10 stop | DOGE | UP | 0.67 | 0.41 | -2.93 |
| 11-18 04:50 | +10 stop | ZEC | UP | 0.60 | 0.37 | -2.64 |
| 11-18 04:49 | +10 stop | ZEC | DOWN | 0.37 | 0.58 | 1.75 |
| 11-18 04:49 | +10 stop | BNB | UP | 0.63 | 0.83 | 1.76 |
| 11-18 04:49 | +10 stop | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-18 04:49 | +10 | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-18 04:49 | +10 stop | NEAR | UP | 0.59 | 0.77 | 1.48 |
| 11-18 04:49 | +20 | NEAR | UP | 0.59 | 0.84 | 2.21 |
| 11-18 04:49 | +15 | NEAR | UP | 0.59 | 0.77 | 1.48 |
| 11-18 04:49 | +10 | NEAR | UP | 0.59 | 0.77 | 1.48 |
