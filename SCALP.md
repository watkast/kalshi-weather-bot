# Range-Scalp Bot

*Updated Thu Nov 05 07:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48202 | 41987 | 6215 (73) | 3 | $-13819.34 | -4.6% |
| **+10¢** | 35992 | 28772 | 7220 (99) | 5 | $-12674.83 | -5.6% |
| **+15¢** | 30164 | 22391 | 7773 (127) | 6 | $-11570.18 | -6.1% |
| **+20¢** | 26797 | 18655 | 8142 (166) | 6 | $-10216.99 | -6.1% |
| **+10¢ (15¢ stop)** | 58731 | 58638 | 93 (56) | 0 | $-21812.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 07:08 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-05 07:08 | +10 stop | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-05 07:08 | +5 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-05 07:07 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-05 07:05 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.07 |
| 11-05 07:05 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-05 07:04 | +10 stop | ZEC | DOWN | 0.51 | 0.36 | -1.85 |
| 11-05 07:04 | +10 | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 11-05 07:04 | +5 | ZEC | DOWN | 0.51 | 0.58 | 0.34 |
| 11-05 07:04 | +5 | XRP | DOWN | 0.37 | 0.53 | 1.28 |
| 11-05 07:04 | +10 stop | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-05 07:04 | +5 | XRP | DOWN | 0.56 | 0.61 | 0.20 |
| 11-05 07:03 | +10 stop | HYPE | DOWN | 0.55 | 0.26 | -3.22 |
| 11-05 07:03 | +10 stop | DOGE | DOWN | 0.62 | 0.35 | -3.03 |
| 11-05 07:02 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 11-05 07:02 | +10 stop | BNB | UP | 0.64 | 0.48 | -1.95 |
| 11-05 07:02 | +10 stop | SOL | UP | 0.63 | 0.41 | -2.54 |
| 11-05 07:02 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-05 07:02 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
| 11-05 07:02 | +20 | ETH | UP | 0.61 | 0.82 | 1.82 |
| 11-05 07:02 | +15 | ETH | UP | 0.61 | 0.78 | 1.40 |
| 11-05 07:02 | +10 | ETH | UP | 0.61 | 0.75 | 1.09 |
| 11-05 07:02 | +5 | ETH | UP | 0.61 | 0.75 | 1.09 |
| 11-05 07:02 | +10 stop | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 11-05 07:02 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-05 07:01 | +10 stop | HYPE | UP | 0.63 | 0.47 | -1.95 |
| 11-05 07:01 | +20 | HYPE | UP | 0.62 | 0.83 | 1.83 |
| 11-05 07:01 | +15 | HYPE | UP | 0.62 | 0.79 | 1.41 |
| 11-05 07:01 | +10 | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 11-05 07:01 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 11-05 07:01 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-05 07:01 | +20 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-05 07:01 | +15 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-05 07:01 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-05 07:01 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-05 07:01 | +10 stop | XRP | DOWN | 0.61 | 0.36 | -2.84 |
| 11-05 07:01 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-05 07:01 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-05 07:01 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-05 07:01 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.32 |
