# Range-Scalp Bot

*Updated Thu Nov 19 17:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65275 | 56985 | 8290 (124) | 3 | $-17444.67 | -4.2% |
| **+10¢** | 48751 | 39048 | 9703 (165) | 3 | $-16257.92 | -5.3% |
| **+15¢** | 40878 | 30411 | 10467 (211) | 4 | $-14650.75 | -5.7% |
| **+20¢** | 36405 | 25409 | 10996 (266) | 6 | $-12962.47 | -5.7% |
| **+10¢ (15¢ stop)** | 79457 | 79293 | 164 (98) | 1 | $-29238.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 17:51 | +10 stop | SOL | DOWN | 0.57 | open |  |
| 11-19 17:51 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.73 |
| 11-19 17:51 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.88 |
| 11-19 17:50 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 11-19 17:50 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-19 17:49 | +20 | HYPE | UP | 0.68 | open |  |
| 11-19 17:49 | +15 | HYPE | UP | 0.68 | open |  |
| 11-19 17:49 | +10 stop | BNB | UP | 0.43 | 0.55 | 0.84 |
| 11-19 17:49 | +10 stop | SOL | UP | 0.54 | 0.35 | -2.24 |
| 11-19 17:49 | +5 | SOL | UP | 0.53 | open |  |
| 11-19 17:48 | +5 | BNB | UP | 0.58 | open |  |
| 11-19 17:48 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-19 17:48 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-19 17:48 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-19 17:48 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-19 17:48 | +10 stop | HYPE | UP | 0.64 | 0.40 | -2.74 |
| 11-19 17:48 | +10 | HYPE | UP | 0.65 | open |  |
| 11-19 17:48 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-19 17:48 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-19 17:48 | +5 | NEAR | DOWN | 0.65 | 0.77 | 0.92 |
| 11-19 17:48 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 17:48 | +15 | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-19 17:48 | +10 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 17:48 | +5 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 17:48 | +5 | XRP | DOWN | 0.55 | 0.67 | 0.85 |
| 11-19 17:48 | +5 | HYPE | UP | 0.69 | open |  |
| 11-19 17:47 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 11-19 17:47 | +5 | SOL | DOWN | 0.49 | 0.62 | 0.95 |
| 11-19 17:47 | +5 | BNB | DOWN | 0.50 | 0.62 | 0.85 |
| 11-19 17:47 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-19 17:47 | +10 stop | HYPE | UP | 0.51 | 0.65 | 1.06 |
| 11-19 17:47 | +20 | HYPE | UP | 0.52 | 0.72 | 1.67 |
| 11-19 17:47 | +15 | HYPE | UP | 0.52 | 0.67 | 1.16 |
| 11-19 17:47 | +10 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-19 17:47 | +5 | HYPE | UP | 0.52 | 0.58 | 0.24 |
| 11-19 17:46 | +10 stop | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 17:46 | +20 | DOGE | DOWN | 0.56 | 0.76 | 1.69 |
| 11-19 17:46 | +15 | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 17:46 | +10 | DOGE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-19 17:46 | +5 | DOGE | DOWN | 0.56 | 0.72 | 1.23 |
