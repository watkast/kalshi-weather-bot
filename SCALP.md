# Range-Scalp Bot

*Updated Sun Nov 08 22:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52886 | 46110 | 6776 (83) | 1 | $-14639.51 | -4.4% |
| **+10¢** | 39488 | 31589 | 7899 (108) | 1 | $-13621.57 | -5.5% |
| **+15¢** | 33083 | 24572 | 8511 (139) | 1 | $-12453.16 | -6.0% |
| **+20¢** | 29428 | 20505 | 8923 (184) | 1 | $-10963.01 | -5.9% |
| **+10¢ (15¢ stop)** | 64410 | 64304 | 106 (63) | 0 | $-23831.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 22:08 | +10 stop | ETH | UP | 0.49 | 0.32 | -2.04 |
| 11-08 22:07 | +10 stop | XRP | UP | 0.68 | 0.86 | 1.55 |
| 11-08 22:07 | +20 | XRP | UP | 0.69 | 0.93 | 2.16 |
| 11-08 22:07 | +15 | XRP | UP | 0.67 | 0.86 | 1.65 |
| 11-08 22:07 | +10 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 11-08 22:07 | +5 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 11-08 22:07 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-08 22:07 | +20 | ZEC | UP | 0.64 | 0.84 | 1.73 |
| 11-08 22:07 | +15 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 11-08 22:07 | +10 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 11-08 22:07 | +5 | ZEC | UP | 0.64 | 0.80 | 1.27 |
| 11-08 22:07 | +10 stop | HYPE | UP | 0.54 | 0.74 | 1.68 |
| 11-08 22:07 | +20 | HYPE | UP | 0.56 | 0.78 | 1.89 |
| 11-08 22:07 | +15 | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-08 22:07 | +10 | HYPE | UP | 0.53 | 0.74 | 1.78 |
| 11-08 22:07 | +5 | HYPE | UP | 0.53 | 0.58 | 0.14 |
| 11-08 22:07 | +10 stop | ETH | DOWN | 0.71 | 0.48 | -2.63 |
| 11-08 22:06 | +10 stop | ETH | UP | 0.57 | 0.39 | -2.15 |
| 11-08 22:06 | +15 | ETH | UP | 0.58 | open |  |
| 11-08 22:06 | +10 | ETH | UP | 0.60 | open |  |
| 11-08 22:06 | +5 | ETH | UP | 0.60 | open |  |
| 11-08 22:01 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-08 22:01 | +20 | ETH | UP | 0.64 | open |  |
| 11-08 22:01 | +15 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 11-08 22:01 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-08 22:01 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 11-08 21:54 | +10 stop | ZEC | UP | 0.55 | 0.15 | -4.27 |
| 11-08 21:53 | +10 stop | ZEC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-08 21:51 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 11-08 21:51 | +5 | ZEC | UP | 0.60 | no | -6.22 |
| 11-08 21:49 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.20 |
| 11-08 21:49 | +10 stop | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-08 21:48 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 11-08 21:48 | +10 stop | NEAR | DOWN | 0.63 | 0.95 | 2.96 |
| 11-08 21:48 | +10 | NEAR | DOWN | 0.63 | 0.95 | 2.96 |
| 11-08 21:48 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 11-08 21:47 | +5 | ZEC | UP | 0.53 | 0.60 | 0.35 |
| 11-08 21:47 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-08 21:47 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 21:47 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
