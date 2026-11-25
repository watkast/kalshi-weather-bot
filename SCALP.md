# Range-Scalp Bot

*Updated Wed Nov 25 07:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71608 | 62508 | 9100 (157) | 6 | $-19032.57 | -4.2% |
| **+10¢** | 53409 | 42778 | 10631 (203) | 8 | $-17653.15 | -5.3% |
| **+15¢** | 44730 | 33285 | 11445 (260) | 9 | $-15685.96 | -5.6% |
| **+20¢** | 39825 | 27770 | 12055 (326) | 9 | $-14095.43 | -5.6% |
| **+10¢ (15¢ stop)** | 87188 | 86985 | 203 (123) | 1 | $-32046.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 07:35 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 11-25 07:35 | +10 stop | BTC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-25 07:34 | +10 stop | ZEC | DOWN | 0.63 | 0.42 | -2.44 |
| 11-25 07:34 | +10 stop | XRP | DOWN | 0.71 | 0.46 | -2.83 |
| 11-25 07:34 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-25 07:34 | +10 stop | HYPE | UP | 0.56 | 0.12 | -4.66 |
| 11-25 07:34 | +10 | HYPE | UP | 0.56 | open |  |
| 11-25 07:33 | +10 stop | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-25 07:33 | +10 stop | BTC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-25 07:33 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.76 |
| 11-25 07:33 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-25 07:33 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-25 07:33 | +5 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 11-25 07:32 | +10 stop | HYPE | UP | 0.53 | 0.66 | 0.96 |
| 11-25 07:32 | +15 | HYPE | UP | 0.55 | open |  |
| 11-25 07:32 | +10 | HYPE | UP | 0.54 | 0.66 | 0.87 |
| 11-25 07:32 | +5 | SOL | UP | 0.50 | 0.59 | 0.55 |
| 11-25 07:32 | +5 | ETH | UP | 0.57 | open |  |
| 11-25 07:32 | +5 | XRP | UP | 0.60 | open |  |
| 11-25 07:32 | +10 stop | ZEC | UP | 0.65 | 0.49 | -1.94 |
| 11-25 07:32 | +20 | ZEC | UP | 0.66 | open |  |
| 11-25 07:32 | +15 | ZEC | UP | 0.66 | open |  |
| 11-25 07:32 | +10 | ZEC | UP | 0.66 | open |  |
| 11-25 07:32 | +5 | ZEC | UP | 0.66 | open |  |
| 11-25 07:32 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-25 07:32 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-25 07:32 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-25 07:32 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-25 07:32 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 11-25 07:32 | +10 stop | SOL | UP | 0.56 | 0.36 | -2.35 |
| 11-25 07:32 | +20 | SOL | UP | 0.56 | open |  |
| 11-25 07:32 | +15 | SOL | UP | 0.56 | open |  |
| 11-25 07:32 | +10 | SOL | UP | 0.57 | open |  |
| 11-25 07:32 | +5 | SOL | UP | 0.57 | 0.62 | 0.15 |
| 11-25 07:31 | +5 | HYPE | UP | 0.71 | open |  |
| 11-25 07:31 | +10 stop | ETH | UP | 0.56 | 0.41 | -1.85 |
| 11-25 07:31 | +20 | ETH | UP | 0.55 | open |  |
| 11-25 07:31 | +15 | ETH | UP | 0.56 | open |  |
| 11-25 07:31 | +10 | ETH | UP | 0.56 | open |  |
| 11-25 07:31 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
