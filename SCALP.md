# Range-Scalp Bot

*Updated Tue Nov 17 19:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63176 | 55112 | 8064 (117) | 9 | $-17177.66 | -4.3% |
| **+10¢** | 47198 | 37761 | 9437 (159) | 9 | $-16046.01 | -5.4% |
| **+15¢** | 39567 | 29392 | 10175 (201) | 9 | $-14540.28 | -5.9% |
| **+20¢** | 35253 | 24574 | 10679 (256) | 9 | $-12788.79 | -5.8% |
| **+10¢ (15¢ stop)** | 76906 | 76750 | 156 (92) | 0 | $-28300.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 19:09 | +10 stop | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 11-17 19:09 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-17 19:09 | +10 stop | BTC | DOWN | 0.43 | 0.55 | 0.84 |
| 11-17 19:09 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-17 19:09 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-17 19:09 | +10 stop | NEAR | UP | 0.65 | 0.88 | 2.03 |
| 11-17 19:08 | +10 stop | HYPE | UP | 0.65 | 0.48 | -2.04 |
| 11-17 19:07 | +10 stop | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-17 19:07 | +10 stop | BTC | UP | 0.62 | 0.37 | -2.84 |
| 11-17 19:06 | +10 stop | NEAR | UP | 0.60 | 0.73 | 0.95 |
| 11-17 19:06 | +10 stop | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 11-17 19:06 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 11-17 19:06 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-17 19:06 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-17 19:05 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 11-17 19:05 | +10 stop | XRP | DOWN | 0.51 | 0.65 | 1.06 |
| 11-17 19:05 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.95 |
| 11-17 19:05 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-17 19:05 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-17 19:04 | +10 stop | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 11-17 19:02 | +10 stop | NEAR | DOWN | 0.69 | 0.45 | -2.76 |
| 11-17 19:02 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-17 19:02 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-17 19:02 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-17 19:02 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-17 19:02 | +10 stop | SOL | DOWN | 0.71 | 0.52 | -2.23 |
| 11-17 19:02 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-17 19:02 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-17 19:02 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-17 19:02 | +5 | SOL | DOWN | 0.70 | open |  |
| 11-17 19:02 | +10 stop | XRP | DOWN | 0.71 | 0.55 | -1.93 |
| 11-17 19:02 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-17 19:02 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-17 19:02 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-17 19:02 | +5 | XRP | DOWN | 0.71 | open |  |
| 11-17 19:01 | +10 stop | DOGE | DOWN | 0.63 | 0.42 | -2.45 |
| 11-17 19:01 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-17 19:01 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-17 19:01 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-17 19:01 | +5 | DOGE | DOWN | 0.63 | open |  |
