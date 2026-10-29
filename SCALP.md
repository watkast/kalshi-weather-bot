# Range-Scalp Bot

*Updated Thu Oct 29 11:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39204 | 34210 | 4994 (49) | 6 | $-11013.77 | -4.5% |
| **+10¢** | 29240 | 23474 | 5766 (71) | 6 | $-9751.18 | -5.3% |
| **+15¢** | 24449 | 18254 | 6195 (98) | 6 | $-8720.63 | -5.7% |
| **+20¢** | 21687 | 15198 | 6489 (127) | 8 | $-7617.38 | -5.6% |
| **+10¢ (15¢ stop)** | 47920 | 47853 | 67 (35) | 4 | $-18191.78 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 11:35 | +5 | BNB | DOWN | 0.56 | 0.62 | 0.25 |
| 10-29 11:34 | +10 stop | ETH | DOWN | 0.57 | 0.33 | -2.74 |
| 10-29 11:34 | +10 | DOGE | DOWN | 0.70 | open |  |
| 10-29 11:34 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-29 11:33 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-29 11:33 | +10 stop | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-29 11:33 | +15 | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-29 11:33 | +10 | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-29 11:33 | +5 | XRP | UP | 0.63 | 0.70 | 0.38 |
| 10-29 11:33 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-29 11:33 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-29 11:33 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 10-29 11:33 | +10 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 10-29 11:33 | +5 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 10-29 11:33 | +10 stop | ZEC | UP | 0.50 | 0.61 | 0.75 |
| 10-29 11:33 | +15 | ZEC | UP | 0.50 | 0.67 | 1.36 |
| 10-29 11:33 | +10 | ZEC | UP | 0.50 | 0.61 | 0.75 |
| 10-29 11:32 | +10 stop | DOGE | UP | 0.60 | 0.43 | -2.05 |
| 10-29 11:32 | +5 | ZEC | UP | 0.69 | open |  |
| 10-29 11:32 | +10 stop | BTC | UP | 0.53 | 0.38 | -1.85 |
| 10-29 11:32 | +20 | BTC | UP | 0.53 | open |  |
| 10-29 11:32 | +15 | BTC | UP | 0.53 | open |  |
| 10-29 11:32 | +10 | BTC | UP | 0.53 | open |  |
| 10-29 11:32 | +5 | BTC | UP | 0.53 | open |  |
| 10-29 11:32 | +10 stop | SOL | UP | 0.58 | 0.28 | -3.33 |
| 10-29 11:32 | +20 | SOL | UP | 0.58 | open |  |
| 10-29 11:32 | +15 | SOL | UP | 0.58 | open |  |
| 10-29 11:32 | +10 | SOL | UP | 0.58 | open |  |
| 10-29 11:32 | +5 | SOL | UP | 0.58 | open |  |
| 10-29 11:31 | +10 stop | ETH | UP | 0.67 | 0.45 | -2.54 |
| 10-29 11:31 | +20 | ETH | UP | 0.67 | open |  |
| 10-29 11:31 | +15 | ETH | UP | 0.67 | open |  |
| 10-29 11:31 | +10 | ETH | UP | 0.67 | open |  |
| 10-29 11:31 | +5 | ETH | UP | 0.67 | open |  |
| 10-29 11:31 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-29 11:31 | +20 | XRP | UP | 0.61 | open |  |
| 10-29 11:31 | +15 | XRP | UP | 0.62 | 0.78 | 1.30 |
| 10-29 11:31 | +10 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-29 11:31 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 10-29 11:31 | +10 stop | DOGE | DOWN | 0.59 | 0.43 | -1.95 |
