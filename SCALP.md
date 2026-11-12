# Range-Scalp Bot

*Updated Thu Nov 12 13:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56944 | 49642 | 7302 (101) | 8 | $-15649.81 | -4.4% |
| **+10¢** | 42553 | 34034 | 8519 (133) | 9 | $-14585.90 | -5.5% |
| **+15¢** | 35679 | 26509 | 9170 (167) | 9 | $-13192.30 | -5.9% |
| **+20¢** | 31785 | 22164 | 9621 (217) | 9 | $-11568.23 | -5.8% |
| **+10¢ (15¢ stop)** | 69424 | 69296 | 128 (78) | 2 | $-25653.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 13:25 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-12 13:25 | +15 | NEAR | UP | 0.66 | open |  |
| 11-12 13:25 | +5 | NEAR | UP | 0.66 | open |  |
| 11-12 13:22 | +10 stop | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 11-12 13:22 | +10 stop | XRP | UP | 0.66 | 0.84 | 1.54 |
| 11-12 13:22 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-12 13:22 | +20 | NEAR | UP | 0.57 | open |  |
| 11-12 13:22 | +15 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 11-12 13:22 | +5 | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 11-12 13:21 | +10 stop | SOL | UP | 0.70 | open |  |
| 11-12 13:20 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.12 |
| 11-12 13:20 | +10 stop | NEAR | DOWN | 0.70 | 0.41 | -3.22 |
| 11-12 13:20 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-12 13:20 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 11-12 13:20 | +10 stop | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 11-12 13:20 | +5 | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-12 13:19 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 11-12 13:19 | +15 | NEAR | DOWN | 0.56 | 0.72 | 1.27 |
| 11-12 13:19 | +10 | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 11-12 13:19 | +5 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-12 13:19 | +10 stop | SOL | DOWN | 0.50 | 0.34 | -1.94 |
| 11-12 13:19 | +10 stop | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 11-12 13:19 | +10 stop | BNB | DOWN | 0.51 | 0.29 | -2.53 |
| 11-12 13:18 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.77 |
| 11-12 13:18 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-12 13:18 | +10 stop | ZEC | DOWN | 0.51 | 0.32 | -2.24 |
| 11-12 13:18 | +20 | ZEC | DOWN | 0.52 | open |  |
| 11-12 13:18 | +15 | ZEC | DOWN | 0.52 | open |  |
| 11-12 13:18 | +10 | ZEC | DOWN | 0.52 | open |  |
| 11-12 13:18 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 11-12 13:17 | +10 stop | HYPE | DOWN | 0.61 | 0.44 | -2.03 |
| 11-12 13:17 | +5 | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 11-12 13:16 | +10 stop | SOL | DOWN | 0.64 | 0.48 | -1.95 |
| 11-12 13:16 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-12 13:16 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-12 13:16 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-12 13:16 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-12 13:16 | +10 stop | ETH | DOWN | 0.56 | 0.35 | -2.44 |
| 11-12 13:16 | +20 | ETH | DOWN | 0.56 | open |  |
| 11-12 13:16 | +15 | ETH | DOWN | 0.56 | open |  |
