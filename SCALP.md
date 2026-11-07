# Range-Scalp Bot

*Updated Sat Nov 07 02:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50351 | 43892 | 6459 (76) | 2 | $-14150.88 | -4.5% |
| **+10¢** | 37566 | 30047 | 7519 (102) | 5 | $-13079.25 | -5.5% |
| **+15¢** | 31459 | 23357 | 8102 (131) | 5 | $-11986.02 | -6.1% |
| **+20¢** | 27966 | 19470 | 8496 (173) | 6 | $-10612.99 | -6.1% |
| **+10¢ (15¢ stop)** | 61307 | 61208 | 99 (58) | 0 | $-22722.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 02:34 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-07 02:34 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-07 02:34 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-07 02:34 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-07 02:34 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-07 02:33 | +10 stop | ZEC | UP | 0.51 | 0.33 | -2.14 |
| 11-07 02:33 | +20 | ZEC | UP | 0.50 | open |  |
| 11-07 02:33 | +15 | ZEC | UP | 0.49 | open |  |
| 11-07 02:33 | +10 | ZEC | UP | 0.49 | open |  |
| 11-07 02:33 | +5 | ZEC | UP | 0.49 | 0.55 | 0.24 |
| 11-07 02:32 | +10 stop | ETH | UP | 0.54 | 0.26 | -3.12 |
| 11-07 02:32 | +20 | ETH | UP | 0.54 | open |  |
| 11-07 02:32 | +15 | ETH | UP | 0.54 | open |  |
| 11-07 02:32 | +10 | ETH | UP | 0.54 | open |  |
| 11-07 02:32 | +5 | ETH | UP | 0.54 | open |  |
| 11-07 02:32 | +10 stop | BTC | UP | 0.54 | 0.33 | -2.44 |
| 11-07 02:32 | +20 | BTC | UP | 0.54 | open |  |
| 11-07 02:32 | +15 | BTC | UP | 0.54 | open |  |
| 11-07 02:32 | +10 | BTC | UP | 0.54 | open |  |
| 11-07 02:32 | +5 | BTC | UP | 0.54 | open |  |
| 11-07 02:31 | +5 | BNB | UP | 0.65 | 0.75 | 0.74 |
| 11-07 02:31 | +10 stop | BNB | UP | 0.60 | 0.75 | 1.19 |
| 11-07 02:31 | +20 | BNB | UP | 0.60 | open |  |
| 11-07 02:31 | +15 | BNB | UP | 0.60 | 0.75 | 1.19 |
| 11-07 02:31 | +10 | BNB | UP | 0.60 | 0.75 | 1.19 |
| 11-07 02:31 | +5 | BNB | UP | 0.60 | 0.69 | 0.58 |
| 11-07 02:31 | +10 stop | HYPE | UP | 0.65 | 0.41 | -2.73 |
| 11-07 02:31 | +20 | HYPE | UP | 0.65 | open |  |
| 11-07 02:31 | +15 | HYPE | UP | 0.65 | open |  |
| 11-07 02:31 | +10 | HYPE | UP | 0.65 | open |  |
| 11-07 02:31 | +5 | HYPE | UP | 0.65 | 0.72 | 0.39 |
| 11-07 02:31 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.24 |
| 11-07 02:31 | +20 | NEAR | UP | 0.65 | open |  |
| 11-07 02:31 | +15 | NEAR | UP | 0.65 | open |  |
| 11-07 02:31 | +10 | NEAR | UP | 0.65 | open |  |
| 11-07 02:31 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 11-07 02:25 | +10 stop | HYPE | DOWN | 0.68 | 0.33 | -3.82 |
| 11-07 02:24 | +10 stop | HYPE | DOWN | 0.48 | 0.80 | 2.90 |
| 11-07 02:22 | +10 stop | HYPE | UP | 0.59 | 0.43 | -1.95 |
| 11-07 02:22 | +15 | HYPE | UP | 0.59 | 0.85 | 2.34 |
