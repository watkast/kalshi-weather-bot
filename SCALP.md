# Range-Scalp Bot

*Updated Tue Nov 10 09:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54465 | 47505 | 6960 (89) | 0 | $-14877.77 | -4.3% |
| **+10¢** | 40699 | 32579 | 8120 (117) | 0 | $-13824.89 | -5.4% |
| **+15¢** | 34114 | 25359 | 8755 (150) | 0 | $-12598.35 | -5.9% |
| **+20¢** | 30377 | 21194 | 9183 (198) | 1 | $-11002.93 | -5.8% |
| **+10¢ (15¢ stop)** | 66372 | 66262 | 110 (66) | 0 | $-24566.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 09:03 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 09:03 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-10 09:03 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 09:03 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 09:03 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 08:58 | +10 stop | NEAR | DOWN | 0.70 | 0.42 | -3.13 |
| 11-10 08:58 | +20 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:58 | +15 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:58 | +10 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:58 | +5 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:57 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-10 08:57 | +15 | ZEC | UP | 0.66 | 0.89 | 2.07 |
| 11-10 08:57 | +10 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-10 08:57 | +5 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-10 08:56 | +10 stop | HYPE | DOWN | 0.52 | 0.09 | -4.50 |
| 11-10 08:56 | +20 | HYPE | DOWN | 0.52 | yes | -5.38 |
| 11-10 08:56 | +15 | HYPE | DOWN | 0.52 | yes | -5.38 |
| 11-10 08:56 | +10 | HYPE | DOWN | 0.52 | yes | -5.38 |
| 11-10 08:56 | +5 | HYPE | DOWN | 0.52 | yes | -5.38 |
| 11-10 08:52 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-10 08:52 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-10 08:52 | +10 | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-10 08:52 | +5 | SOL | UP | 0.69 | 0.75 | 0.31 |
| 11-10 08:52 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 08:52 | +10 stop | DOGE | DOWN | 0.67 | 0.40 | -3.03 |
| 11-10 08:52 | +10 stop | HYPE | UP | 0.46 | 0.60 | 1.05 |
| 11-10 08:51 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-10 08:51 | +10 stop | NEAR | UP | 0.47 | 0.22 | -2.81 |
| 11-10 08:51 | +10 stop | ZEC | UP | 0.58 | 0.38 | -2.35 |
| 11-10 08:50 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-10 08:49 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 11-10 08:49 | +10 stop | DOGE | DOWN | 0.65 | 0.47 | -2.14 |
| 11-10 08:48 | +10 stop | NEAR | DOWN | 0.59 | 0.30 | -3.22 |
| 11-10 08:48 | +10 stop | ZEC | DOWN | 0.55 | 0.33 | -2.54 |
| 11-10 08:48 | +10 stop | HYPE | UP | 0.53 | 0.67 | 1.06 |
| 11-10 08:48 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.86 |
| 11-10 08:47 | +10 stop | XRP | UP | 0.58 | 0.31 | -3.03 |
| 11-10 08:47 | +20 | XRP | UP | 0.58 | 0.81 | 2.01 |
| 11-10 08:47 | +15 | XRP | UP | 0.57 | 0.81 | 2.11 |
| 11-10 08:47 | +10 | XRP | UP | 0.57 | 0.71 | 1.07 |
