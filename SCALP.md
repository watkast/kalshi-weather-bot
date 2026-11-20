# Range-Scalp Bot

*Updated Fri Nov 20 00:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65504 | 57180 | 8324 (124) | 1 | $-17532.06 | -4.3% |
| **+10¢** | 48918 | 39184 | 9734 (165) | 1 | $-16314.12 | -5.3% |
| **+15¢** | 41024 | 30524 | 10500 (211) | 2 | $-14679.93 | -5.7% |
| **+20¢** | 36522 | 25490 | 11032 (266) | 6 | $-13013.85 | -5.7% |
| **+10¢ (15¢ stop)** | 79748 | 79584 | 164 (98) | 1 | $-29348.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 00:02 | +10 stop | ZEC | UP | 0.69 | open |  |
| 11-20 00:01 | +5 | ZEC | UP | 0.68 | open |  |
| 11-20 00:01 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-20 00:01 | +20 | NEAR | UP | 0.67 | open |  |
| 11-20 00:01 | +15 | NEAR | UP | 0.67 | open |  |
| 11-20 00:01 | +10 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-20 00:01 | +5 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-20 00:01 | +10 stop | ZEC | DOWN | 0.52 | 0.33 | -2.24 |
| 11-20 00:01 | +20 | ZEC | DOWN | 0.52 | open |  |
| 11-20 00:01 | +15 | ZEC | DOWN | 0.52 | open |  |
| 11-20 00:01 | +10 | ZEC | DOWN | 0.52 | open |  |
| 11-20 00:01 | +5 | ZEC | DOWN | 0.52 | 0.61 | 0.55 |
| 11-20 00:00 | +10 stop | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-20 00:00 | +20 | BTC | UP | 0.63 | open |  |
| 11-20 00:00 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-20 00:00 | +10 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-20 00:00 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 11-20 00:00 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-20 00:00 | +20 | ETH | UP | 0.63 | open |  |
| 11-20 00:00 | +15 | ETH | UP | 0.63 | 0.79 | 1.31 |
| 11-20 00:00 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-20 00:00 | +5 | ETH | UP | 0.63 | 0.71 | 0.48 |
| 11-20 00:00 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.72 |
| 11-20 00:00 | +20 | DOGE | UP | 0.67 | open |  |
| 11-20 00:00 | +15 | DOGE | UP | 0.67 | 0.84 | 1.45 |
| 11-20 00:00 | +10 | DOGE | UP | 0.67 | 0.77 | 0.72 |
| 11-20 00:00 | +5 | DOGE | UP | 0.67 | 0.75 | 0.51 |
| 11-20 00:00 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-20 00:00 | +20 | BNB | UP | 0.68 | open |  |
| 11-20 00:00 | +15 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 11-20 00:00 | +10 | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-20 00:00 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-20 00:00 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-20 00:00 | +20 | HYPE | UP | 0.64 | 0.85 | 1.84 |
| 11-20 00:00 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-20 00:00 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-20 00:00 | +5 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-19 23:56 | +10 stop | BTC | UP | 0.60 | 0.36 | -2.74 |
| 11-19 23:56 | +20 | BTC | UP | 0.60 | no | -6.17 |
| 11-19 23:56 | +15 | BTC | UP | 0.60 | no | -6.17 |
