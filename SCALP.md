# Range-Scalp Bot

*Updated Sun Nov 01 22:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44019 | 38339 | 5680 (65) | 0 | $-12680.49 | -4.6% |
| **+10¢** | 32848 | 26287 | 6561 (86) | 0 | $-11415.65 | -5.5% |
| **+15¢** | 27489 | 20428 | 7061 (113) | 0 | $-10428.09 | -6.0% |
| **+20¢** | 24417 | 17023 | 7394 (147) | 0 | $-9191.06 | -6.0% |
| **+10¢ (15¢ stop)** | 53692 | 53606 | 86 (51) | 0 | $-20328.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 22:16 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-01 22:16 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.90 |
| 11-01 22:16 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.90 |
| 11-01 22:16 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-01 22:16 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-01 22:04 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 22:04 | +10 stop | SOL | UP | 0.54 | 0.36 | -2.15 |
| 11-01 22:04 | +10 stop | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 11-01 22:03 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 11-01 22:03 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 11-01 22:02 | +10 stop | NEAR | DOWN | 0.49 | 0.62 | 0.95 |
| 11-01 22:02 | +10 stop | ZEC | DOWN | 0.65 | 0.48 | -2.04 |
| 11-01 22:02 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-01 22:02 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-01 22:02 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 11-01 22:02 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 11-01 22:02 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-01 22:02 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 11-01 22:02 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-01 22:02 | +5 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-01 22:01 | +10 stop | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 22:01 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-01 22:01 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 22:01 | +10 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 22:01 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 11-01 22:01 | +10 stop | BNB | DOWN | 0.68 | 0.82 | 1.16 |
| 11-01 22:01 | +20 | BNB | DOWN | 0.68 | 0.96 | 2.60 |
| 11-01 22:01 | +15 | BNB | DOWN | 0.68 | 0.86 | 1.58 |
| 11-01 22:01 | +10 | BNB | DOWN | 0.68 | 0.82 | 1.16 |
| 11-01 22:01 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.64 |
| 11-01 22:01 | +10 stop | ZEC | UP | 0.57 | 0.38 | -2.25 |
| 11-01 22:01 | +20 | ZEC | UP | 0.57 | no | -5.88 |
| 11-01 22:01 | +15 | ZEC | UP | 0.57 | no | -5.88 |
| 11-01 22:01 | +10 | ZEC | UP | 0.57 | no | -5.88 |
| 11-01 22:01 | +5 | ZEC | UP | 0.57 | no | -5.88 |
| 11-01 22:01 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-01 22:01 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-01 22:01 | +15 | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-01 22:01 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-01 22:01 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
