# Range-Scalp Bot

*Updated Tue Nov 17 16:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63019 | 54968 | 8051 (117) | 1 | $-17179.77 | -4.3% |
| **+10¢** | 47070 | 37653 | 9417 (159) | 1 | $-16033.36 | -5.4% |
| **+15¢** | 39456 | 29302 | 10154 (201) | 1 | $-14546.10 | -5.9% |
| **+20¢** | 35156 | 24508 | 10648 (256) | 1 | $-12725.23 | -5.8% |
| **+10¢ (15¢ stop)** | 76683 | 76527 | 156 (92) | 1 | $-28245.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 16:37 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-17 16:37 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-17 16:37 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-17 16:37 | +5 | BTC | DOWN | 0.68 | open |  |
| 11-17 16:35 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.87 |
| 11-17 16:35 | +10 stop | BTC | UP | 0.55 | 0.37 | -2.15 |
| 11-17 16:34 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-17 16:34 | +15 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 11-17 16:34 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-17 16:34 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-17 16:34 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-17 16:34 | +15 | DOGE | DOWN | 0.66 | 0.84 | 1.54 |
| 11-17 16:34 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-17 16:34 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-17 16:34 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 16:34 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-17 16:34 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 16:34 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-17 16:34 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 11-17 16:32 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-17 16:32 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-17 16:32 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 16:32 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.64 |
| 11-17 16:32 | +5 | ETH | DOWN | 0.67 | 0.75 | 0.50 |
| 11-17 16:32 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.42 |
| 11-17 16:31 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-17 16:31 | +20 | XRP | DOWN | 0.60 | 0.81 | 1.82 |
| 11-17 16:31 | +15 | XRP | DOWN | 0.60 | 0.78 | 1.50 |
| 11-17 16:31 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-17 16:31 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-17 16:31 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-17 16:31 | +20 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 11-17 16:31 | +15 | BNB | DOWN | 0.59 | 0.76 | 1.40 |
| 11-17 16:31 | +10 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-17 16:31 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-17 16:31 | +10 stop | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-17 16:31 | +20 | HYPE | DOWN | 0.56 | 0.80 | 2.10 |
| 11-17 16:31 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-17 16:31 | +10 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-17 16:31 | +5 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
