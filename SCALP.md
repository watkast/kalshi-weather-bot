# Range-Scalp Bot

*Updated Fri Nov 13 00:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57536 | 50172 | 7364 (101) | 3 | $-15728.27 | -4.3% |
| **+10¢** | 43007 | 34409 | 8598 (133) | 7 | $-14665.65 | -5.4% |
| **+15¢** | 36051 | 26797 | 9254 (167) | 8 | $-13234.39 | -5.9% |
| **+20¢** | 32119 | 22410 | 9709 (217) | 8 | $-11590.99 | -5.8% |
| **+10¢ (15¢ stop)** | 70159 | 70031 | 128 (78) | 3 | $-25849.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 00:32 | +10 stop | HYPE | UP | 0.62 | open |  |
| 11-13 00:32 | +10 stop | XRP | DOWN | 0.46 | 0.57 | 0.74 |
| 11-13 00:32 | +10 stop | DOGE | DOWN | 0.50 | open |  |
| 11-13 00:32 | +10 stop | BNB | DOWN | 0.47 | open |  |
| 11-13 00:32 | +10 stop | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-13 00:32 | +5 | DOGE | DOWN | 0.49 | 0.58 | 0.54 |
| 11-13 00:32 | +5 | NEAR | DOWN | 0.40 | 0.59 | 1.56 |
| 11-13 00:31 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 11-13 00:31 | +10 stop | ZEC | UP | 0.50 | 0.64 | 1.05 |
| 11-13 00:31 | +20 | ZEC | UP | 0.54 | 0.76 | 1.89 |
| 11-13 00:31 | +15 | ZEC | UP | 0.55 | 0.76 | 1.79 |
| 11-13 00:31 | +10 | ZEC | UP | 0.55 | 0.76 | 1.79 |
| 11-13 00:31 | +5 | ZEC | UP | 0.55 | 0.64 | 0.55 |
| 11-13 00:31 | +10 stop | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-13 00:31 | +20 | NEAR | UP | 0.49 | open |  |
| 11-13 00:31 | +15 | NEAR | UP | 0.49 | open |  |
| 11-13 00:31 | +10 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-13 00:31 | +5 | NEAR | UP | 0.49 | 0.54 | 0.14 |
| 11-13 00:31 | +10 stop | XRP | UP | 0.49 | 0.33 | -1.94 |
| 11-13 00:31 | +20 | XRP | UP | 0.49 | open |  |
| 11-13 00:31 | +15 | XRP | UP | 0.48 | open |  |
| 11-13 00:31 | +10 | XRP | UP | 0.48 | open |  |
| 11-13 00:31 | +5 | XRP | UP | 0.48 | 0.55 | 0.32 |
| 11-13 00:31 | +10 stop | BTC | UP | 0.59 | 0.35 | -2.73 |
| 11-13 00:31 | +20 | BTC | UP | 0.59 | open |  |
| 11-13 00:31 | +15 | BTC | UP | 0.59 | open |  |
| 11-13 00:31 | +10 | BTC | UP | 0.59 | open |  |
| 11-13 00:31 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-13 00:31 | +10 stop | DOGE | UP | 0.51 | 0.35 | -1.94 |
| 11-13 00:31 | +20 | DOGE | UP | 0.51 | open |  |
| 11-13 00:31 | +15 | DOGE | UP | 0.51 | open |  |
| 11-13 00:31 | +10 | DOGE | UP | 0.51 | open |  |
| 11-13 00:31 | +5 | DOGE | UP | 0.51 | 0.57 | 0.24 |
| 11-13 00:31 | +10 stop | HYPE | UP | 0.61 | 0.46 | -1.85 |
| 11-13 00:31 | +20 | HYPE | UP | 0.61 | open |  |
| 11-13 00:31 | +15 | HYPE | UP | 0.61 | open |  |
| 11-13 00:31 | +10 | HYPE | UP | 0.61 | open |  |
| 11-13 00:31 | +5 | HYPE | UP | 0.61 | open |  |
| 11-13 00:31 | +10 stop | SOL | UP | 0.58 | 0.32 | -2.94 |
| 11-13 00:31 | +20 | SOL | UP | 0.58 | open |  |
