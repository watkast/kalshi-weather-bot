# Range-Scalp Bot

*Updated Sun Nov 22 19:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69003 | 60219 | 8784 (145) | 7 | $-18509.20 | -4.3% |
| **+10¢** | 51488 | 41230 | 10258 (188) | 7 | $-17150.56 | -5.3% |
| **+15¢** | 43150 | 32090 | 11060 (240) | 7 | $-15398.34 | -5.7% |
| **+20¢** | 38420 | 26798 | 11622 (299) | 7 | $-13692.16 | -5.7% |
| **+10¢ (15¢ stop)** | 84023 | 83834 | 189 (117) | 1 | $-30954.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 19:26 | +10 stop | ETH | DOWN | 0.67 | 0.49 | -2.14 |
| 11-22 19:24 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-22 19:23 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-22 19:23 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-22 19:22 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 11-22 19:22 | +10 stop | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-22 19:21 | +10 stop | HYPE | DOWN | 0.67 | 0.49 | -2.09 |
| 11-22 19:20 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 11-22 19:20 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-22 19:20 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-22 19:20 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 19:20 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.03 |
| 11-22 19:20 | +10 stop | HYPE | DOWN | 0.56 | 0.70 | 1.11 |
| 11-22 19:19 | +10 stop | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 11-22 19:19 | +10 stop | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 19:18 | +10 stop | ZEC | UP | 0.51 | 0.35 | -1.94 |
| 11-22 19:17 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 19:17 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-22 19:17 | +5 | HYPE | UP | 0.62 | 0.69 | 0.39 |
| 11-22 19:16 | +10 stop | HYPE | UP | 0.61 | 0.40 | -2.44 |
| 11-22 19:16 | +20 | HYPE | UP | 0.61 | 0.81 | 1.72 |
| 11-22 19:16 | +15 | HYPE | UP | 0.61 | 0.81 | 1.72 |
| 11-22 19:16 | +10 | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 11-22 19:16 | +5 | HYPE | UP | 0.61 | 0.66 | 0.17 |
| 11-22 19:16 | +5 | BNB | UP | 0.54 | open |  |
| 11-22 19:16 | +10 stop | NEAR | UP | 0.64 | 0.36 | -3.14 |
| 11-22 19:16 | +20 | NEAR | UP | 0.64 | open |  |
| 11-22 19:16 | +15 | NEAR | UP | 0.64 | open |  |
| 11-22 19:16 | +10 | NEAR | UP | 0.64 | open |  |
| 11-22 19:16 | +5 | NEAR | UP | 0.64 | open |  |
| 11-22 19:16 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-22 19:16 | +20 | ETH | UP | 0.65 | open |  |
| 11-22 19:16 | +15 | ETH | UP | 0.65 | open |  |
| 11-22 19:16 | +10 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-22 19:16 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-22 19:16 | +10 stop | BNB | UP | 0.54 | 0.34 | -2.32 |
| 11-22 19:16 | +20 | BNB | UP | 0.54 | open |  |
| 11-22 19:16 | +15 | BNB | UP | 0.53 | open |  |
| 11-22 19:16 | +10 | BNB | UP | 0.53 | open |  |
| 11-22 19:16 | +5 | BNB | UP | 0.52 | 0.58 | 0.24 |
