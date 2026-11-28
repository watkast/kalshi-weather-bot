# Range-Scalp Bot

*Updated Sat Nov 28 03:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74314 | 64872 | 9442 (171) | 0 | $-19679.47 | -4.2% |
| **+10¢** | 55361 | 44326 | 11035 (217) | 0 | $-18312.34 | -5.3% |
| **+15¢** | 46357 | 34474 | 11883 (275) | 0 | $-16353.46 | -5.6% |
| **+20¢** | 41254 | 28739 | 12515 (342) | 0 | $-14758.89 | -5.7% |
| **+10¢ (15¢ stop)** | 90439 | 90220 | 219 (135) | 0 | $-33393.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 03:34 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-28 03:34 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-28 03:34 | +5 | BTC | UP | 0.67 | 0.74 | 0.40 |
| 11-28 03:34 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-28 03:34 | +10 stop | ZEC | UP | 0.63 | 0.77 | 1.10 |
| 11-28 03:34 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 11-28 03:33 | +5 | NEAR | UP | 0.65 | 0.73 | 0.54 |
| 11-28 03:32 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-28 03:32 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 11-28 03:32 | +10 stop | XRP | UP | 0.64 | 0.85 | 1.84 |
| 11-28 03:32 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-28 03:32 | +10 stop | ZEC | DOWN | 0.60 | 0.40 | -2.34 |
| 11-28 03:32 | +20 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-28 03:32 | +15 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-28 03:32 | +10 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-28 03:32 | +5 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 11-28 03:32 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-28 03:32 | +20 | BTC | UP | 0.65 | 0.85 | 1.75 |
| 11-28 03:32 | +15 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-28 03:32 | +10 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-28 03:32 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 11-28 03:32 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
| 11-28 03:32 | +20 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 11-28 03:32 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
| 11-28 03:32 | +10 | SOL | UP | 0.65 | 0.76 | 0.81 |
| 11-28 03:32 | +5 | SOL | UP | 0.65 | 0.71 | 0.29 |
| 11-28 03:32 | +5 | DOGE | UP | 0.69 | 0.76 | 0.44 |
| 11-28 03:32 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-28 03:31 | +10 stop | BNB | DOWN | 0.51 | 0.35 | -1.96 |
| 11-28 03:31 | +20 | BNB | DOWN | 0.51 | yes | -5.30 |
| 11-28 03:31 | +15 | BNB | DOWN | 0.51 | yes | -5.30 |
| 11-28 03:31 | +10 | BNB | DOWN | 0.51 | yes | -5.30 |
| 11-28 03:31 | +5 | BNB | DOWN | 0.51 | 0.61 | 0.65 |
| 11-28 03:31 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-28 03:31 | +20 | HYPE | UP | 0.67 | 0.91 | 2.20 |
| 11-28 03:31 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-28 03:31 | +10 | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-28 03:31 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 11-28 03:31 | +10 stop | NEAR | UP | 0.48 | 0.63 | 1.10 |
| 11-28 03:31 | +5 | NEAR | UP | 0.49 | 0.57 | 0.44 |
