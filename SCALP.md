# Range-Scalp Bot

*Updated Mon Nov 16 20:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62206 | 54273 | 7933 (117) | 2 | $-16814.67 | -4.3% |
| **+10¢** | 46450 | 37167 | 9283 (159) | 2 | $-15683.82 | -5.4% |
| **+15¢** | 38921 | 28906 | 10015 (200) | 2 | $-14291.43 | -5.9% |
| **+20¢** | 34695 | 24193 | 10502 (255) | 2 | $-12465.88 | -5.7% |
| **+10¢ (15¢ stop)** | 75714 | 75558 | 156 (92) | 2 | $-27943.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 20:30 | +10 stop | XRP | UP | 0.59 | open |  |
| 11-16 20:30 | +20 | XRP | UP | 0.59 | open |  |
| 11-16 20:30 | +15 | XRP | UP | 0.59 | open |  |
| 11-16 20:30 | +10 | XRP | UP | 0.59 | open |  |
| 11-16 20:30 | +5 | XRP | UP | 0.59 | open |  |
| 11-16 20:30 | +10 stop | BNB | UP | 0.53 | open |  |
| 11-16 20:30 | +20 | BNB | UP | 0.53 | open |  |
| 11-16 20:30 | +15 | BNB | UP | 0.53 | open |  |
| 11-16 20:30 | +10 | BNB | UP | 0.53 | open |  |
| 11-16 20:30 | +5 | BNB | UP | 0.53 | open |  |
| 11-16 20:28 | +10 stop | SOL | DOWN | 0.67 | 0.95 | 2.58 |
| 11-16 20:28 | +20 | SOL | DOWN | 0.68 | 0.95 | 2.48 |
| 11-16 20:28 | +15 | SOL | DOWN | 0.67 | 0.95 | 2.58 |
| 11-16 20:28 | +10 | SOL | DOWN | 0.67 | 0.95 | 2.58 |
| 11-16 20:28 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 20:28 | +5 | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-16 20:27 | +10 stop | SOL | DOWN | 0.17 | 0.58 | 3.82 |
| 11-16 20:27 | +20 | SOL | DOWN | 0.17 | 0.58 | 3.82 |
| 11-16 20:27 | +15 | SOL | DOWN | 0.17 | 0.58 | 3.82 |
| 11-16 20:27 | +10 | SOL | DOWN | 0.20 | 0.58 | 3.50 |
| 11-16 20:27 | +5 | SOL | DOWN | 0.20 | 0.58 | 3.50 |
| 11-16 20:26 | +10 stop | BTC | UP | 0.61 | 0.88 | 2.45 |
| 11-16 20:26 | +20 | BTC | UP | 0.61 | 0.88 | 2.45 |
| 11-16 20:26 | +15 | BTC | UP | 0.61 | 0.88 | 2.45 |
| 11-16 20:22 | +15 | BTC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-16 20:21 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 20:21 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-16 20:20 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 11-16 20:20 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-16 20:19 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 20:19 | +15 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-16 20:19 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 20:19 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 20:19 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.22 |
| 11-16 20:19 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 20:19 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 20:19 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-16 20:19 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 11-16 20:19 | +10 | BTC | UP | 0.64 | 0.88 | 2.15 |
| 11-16 20:19 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
