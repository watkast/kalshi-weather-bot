# Range-Scalp Bot

*Updated Mon Nov 16 20:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62198 | 54265 | 7933 (117) | 4 | $-16822.13 | -4.3% |
| **+10¢** | 46443 | 37160 | 9283 (159) | 5 | $-15695.78 | -5.4% |
| **+15¢** | 38910 | 28895 | 10015 (200) | 7 | $-14311.53 | -5.9% |
| **+20¢** | 34685 | 24183 | 10502 (255) | 7 | $-12488.18 | -5.7% |
| **+10¢ (15¢ stop)** | 75706 | 75550 | 156 (92) | 4 | $-27956.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 20:20 | +5 | ETH | DOWN | 0.60 | open |  |
| 11-16 20:20 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 11-16 20:19 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-16 20:19 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-16 20:19 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-16 20:19 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-16 20:19 | +5 | HYPE | DOWN | 0.69 | open |  |
| 11-16 20:19 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-16 20:19 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-16 20:19 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-16 20:19 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 11-16 20:19 | +10 | BTC | UP | 0.64 | open |  |
| 11-16 20:19 | +5 | BTC | UP | 0.64 | open |  |
| 11-16 20:18 | +5 | ETH | DOWN | 0.55 | 0.62 | 0.35 |
| 11-16 20:18 | +5 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-16 20:18 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-16 20:18 | +10 | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-16 20:18 | +5 | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-16 20:17 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-16 20:17 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-16 20:17 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 20:17 | +10 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-16 20:17 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-16 20:16 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 11-16 20:16 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-16 20:16 | +15 | HYPE | DOWN | 0.66 | open |  |
| 11-16 20:16 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-16 20:16 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 20:16 | +10 stop | ZEC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-16 20:16 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-16 20:16 | +15 | ZEC | DOWN | 0.60 | open |  |
| 11-16 20:16 | +10 | ZEC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-16 20:16 | +5 | ZEC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-16 20:16 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-16 20:16 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-16 20:16 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-16 20:16 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 20:16 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 11-16 20:16 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-16 20:16 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
