# Range-Scalp Bot

*Updated Mon Nov 23 22:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70211 | 61274 | 8937 (147) | 4 | $-18848.16 | -4.3% |
| **+10¢** | 52391 | 41953 | 10438 (190) | 2 | $-17478.78 | -5.3% |
| **+15¢** | 43899 | 32659 | 11240 (246) | 2 | $-15555.16 | -5.6% |
| **+20¢** | 39081 | 27251 | 11830 (311) | 4 | $-13933.80 | -5.7% |
| **+10¢ (15¢ stop)** | 85528 | 85332 | 196 (118) | 0 | $-31476.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 22:38 | +10 stop | HYPE | UP | 0.54 | 0.68 | 1.06 |
| 11-23 22:37 | +5 | ZEC | DOWN | 0.58 | open |  |
| 11-23 22:37 | +10 stop | ZEC | DOWN | 0.55 | 0.39 | -1.95 |
| 11-23 22:37 | +5 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-23 22:36 | +10 stop | BNB | DOWN | 0.57 | 0.76 | 1.59 |
| 11-23 22:36 | +15 | BNB | DOWN | 0.57 | 0.76 | 1.59 |
| 11-23 22:36 | +10 | BNB | DOWN | 0.57 | 0.76 | 1.59 |
| 11-23 22:36 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-23 22:36 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-23 22:36 | +15 | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 11-23 22:36 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-23 22:36 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 11-23 22:36 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-23 22:34 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 11-23 22:34 | +10 | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-23 22:34 | +20 | NEAR | UP | 0.55 | open |  |
| 11-23 22:34 | +15 | NEAR | UP | 0.58 | open |  |
| 11-23 22:34 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 22:34 | +20 | ETH | DOWN | 0.71 | 0.91 | 1.81 |
| 11-23 22:34 | +15 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-23 22:34 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 22:34 | +5 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 22:33 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-23 22:33 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 22:33 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 11-23 22:33 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 22:33 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 22:33 | +5 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 22:33 | +10 stop | NEAR | UP | 0.65 | 0.50 | -1.84 |
| 11-23 22:33 | +10 | NEAR | UP | 0.65 | open |  |
| 11-23 22:33 | +5 | NEAR | UP | 0.64 | open |  |
| 11-23 22:33 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-23 22:33 | +20 | SOL | DOWN | 0.57 | 0.82 | 2.21 |
| 11-23 22:33 | +15 | SOL | DOWN | 0.57 | 0.82 | 2.21 |
| 11-23 22:33 | +10 | SOL | DOWN | 0.59 | 0.82 | 2.02 |
| 11-23 22:33 | +5 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-23 22:33 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 11-23 22:33 | +10 stop | XRP | DOWN | 0.62 | 0.88 | 2.35 |
| 11-23 22:33 | +10 | XRP | DOWN | 0.62 | 0.88 | 2.35 |
| 11-23 22:33 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.47 |
